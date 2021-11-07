from dataclasses import dataclass, field
from pathlib import Path
from typing import (
    Callable,
    Final,
    Iterable,
    List,
    Literal,
    Optional,
    TypeVar,
    Union,
)
from .lib import OutlineNode, WithPage, add_outlines, pikepdf

_T = TypeVar("_T", contravariant=True)


def _filter_indices(
    predicate: Callable[[int, _T], bool], iterable: Iterable[_T]
) -> List[int]:
    return [i for i, x in enumerate(iterable) if predicate(i, x)]


def _last_index(
    predicate: Callable[[int, _T], bool], iterable: Iterable[_T]
) -> Optional[int]:
    return next(reversed(_filter_indices(predicate, iterable)), None)


def _to_letter(number: int) -> str:
    return chr(number + 65)


# region Chapters


@dataclass
class Exercise:
    start_page: int
    name: str
    exercise_page: Optional[int] = None


@dataclass
class ExercisesChapter:
    name: str
    exercises: List[Exercise] = field(default_factory=list)
    review_page: Optional[int] = None


@dataclass
class RevisionChapter:
    multiple_choice_page: int
    extended_response_page: int


_ChapterData = Union[ExercisesChapter, RevisionChapter]


@dataclass
class Chapter(WithPage):
    data: _ChapterData


def _revision_title(start: int, end: int) -> str:
    return f"Revision of Chapters {start}–{end}"


def _get_chapter_outlines(
    chapters: List[Chapter], final_revision: bool
) -> List[OutlineNode]:
    if final_revision:
        last_revision_index = _last_index(
            lambda _, chapter: isinstance(chapter.data, RevisionChapter), chapters
        )
    # Appendices (e.g. Appendix A) don't have a review section
    appendices_indices = _filter_indices(
        lambda _, chapter: isinstance(chapter.data, ExercisesChapter)
        and not chapter.data.review_page,
        chapters,
    )

    def outline_tree(i: int, chapter: Chapter) -> OutlineNode:
        number = i + 1
        page = chapter.page
        data = chapter.data

        title_prefix: str
        title: str
        children: List[OutlineNode]

        if isinstance(data, ExercisesChapter):
            # e.g. Chapter 1: Preliminary topics

            title = data.name

            def exercise_outlines(
                get_exercise_str: Callable[[int], str]
            ) -> List[OutlineNode]:
                def exercise_outline(j: int, exercise: Exercise) -> OutlineNode:
                    exercise_str = get_exercise_str(j)
                    return OutlineNode(
                        exercise.start_page,
                        f"{exercise_str} {exercise.name}",
                        []
                        if exercise.exercise_page is None
                        else [
                            OutlineNode(
                                exercise.exercise_page, f"Exercise {exercise_str}"
                            )
                        ],
                    )

                # inlining it causes type error
                # I think it's because technically data can be mutated to
                # become a RevisionChapter instead of an ExercisesChapter
                # because generators are lazy
                it = enumerate(data.exercises)
                return list(exercise_outline(j, exercise) for j, exercise in it)

            if data.review_page is None:
                # Appendix
                letter = _to_letter(appendices_indices.index(i))
                title_prefix = f"Appendix {letter}"
                # A1, A2, etc.
                children = exercise_outlines(lambda j: f"{letter}{j}")
            else:
                # Normal chapter
                title_prefix = f"Chapter {number}"
                # 1A, 1B, etc.
                children = exercise_outlines(lambda j: f"{number}{_to_letter(j)}") + [
                    OutlineNode(data.review_page, "Review")
                ]
        else:
            # e.g. Chapter 5: Revision of Chapters 1–4

            title_prefix = f"Chapter {number}"
            if final_revision and i == last_revision_index:
                # Final revision of all chapters
                # e.g. Chapter 18: Revision of Chapters 1–17
                title = _revision_title(1, len(chapters) - 1)
            else:
                # Normal revision chapter
                # e.g. Chapter 5: Revision of Chapters 1–4
                previous_revision_index = _last_index(
                    lambda j, ch: j < i and isinstance(ch.data, RevisionChapter),
                    chapters,
                )
                title = _revision_title(
                    1
                    if previous_revision_index is None
                    else previous_revision_index
                    + 2,  # + 1 (next chapter) + 1 (indices start at 0)
                    i,
                )
            children = [
                # Tech-free starts on first page
                OutlineNode(page, f"{number}A Technology-free questions"),
                OutlineNode(
                    data.multiple_choice_page, f"{number}B Multiple-choice questions"
                ),
                OutlineNode(
                    data.extended_response_page,
                    f"{number}C Extended-response questions",
                ),
            ]

        return OutlineNode(page, f"{title_prefix}: {title}", children)

    return list(outline_tree(i, chapter) for i, chapter in enumerate(chapters))


# endregion

# region Answers

_Review = Literal["Review"]
_Letter = Literal["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
_AnswerExercise = Union[_Letter, _Review, int]
REVIEW: Final[_Review] = "Review"


@dataclass
class ExercisesAnswer:
    page: int
    start: _AnswerExercise
    end: Optional[_AnswerExercise] = None


_AnswerData = Union[List[ExercisesAnswer], _Review]


@dataclass
class ChapterAnswers(WithPage):
    data: _AnswerData


def _is_appendix_answer(answers: List[ExercisesAnswer]) -> bool:
    # Appendices don't have a review, so neither do the answers
    return all(answer.start != REVIEW and answer.end != REVIEW for answer in answers)


def _get_answer_outlines(answers: List[ChapterAnswers]) -> List[OutlineNode]:
    appendices_indices = _filter_indices(
        lambda _, answer: answer.data != REVIEW and _is_appendix_answer(answer.data),
        answers,
    )

    def answer_outline(i: int, answer: ChapterAnswers) -> OutlineNode:
        number = i + 1
        page = answer.page

        if answer.data == REVIEW:
            # Answers for a review chapter
            return OutlineNode(page, f"Chapter {number}")

        data = answer.data

        def children(chapter: Union[int, str]) -> List[OutlineNode]:
            return [
                OutlineNode(
                    exercise.page,
                    f'{chapter}{exercise.start}{"" if exercise.end is None else f"–{exercise.end}"}',
                )
                for exercise in data
            ]

        if _is_appendix_answer(data):
            letter = _to_letter(appendices_indices.index(i))
            return OutlineNode(page, f"Appendix {letter}", children(letter))
        return OutlineNode(page, f"Chapter {number}", children(number))

    return list(answer_outline(i, answer) for i, answer in enumerate(answers))


# endregion


def add_maths_textbook_outlines(
    input: Path,
    output: Path,
    answers_output: Path,
    introduction: int,
    acknowledgments: int,
    overview: int,
    glossary: int,
    chapters: List[Chapter],
    answers: List[ChapterAnswers],
    contents: int = 3,
    final_revision: bool = True,
):
    answer_outlines = _get_answer_outlines(answers)
    answers_start_page = answers[0].page
    with pikepdf.open(input) as pdf:
        add_outlines(
            pdf,
            output,
            [
                OutlineNode(contents, "Contents"),
                OutlineNode(introduction, "Introduction"),
                OutlineNode(acknowledgments, "Acknowledgments"),
                OutlineNode(
                    overview,
                    "An overview of the Cambridge complete teacher and learning resource",
                ),
            ]
            + _get_chapter_outlines(chapters, final_revision)
            + [OutlineNode(glossary, "Glossary")]
            + [OutlineNode(answers_start_page, "Answers", answer_outlines)],
            "main PDF",
        )

        answers_pdf = pikepdf.new()
        answers_pdf.pages.extend(pdf.pages[answers_start_page - 1 :])
        add_outlines(
            answers_pdf,
            answers_output,
            # Adjust page numbers
            (
                n.map(lambda page, label: (page - answers_start_page + 1, label))
                for n in answer_outlines
            ),
            "answers PDF",
        )

    print("Complete")
