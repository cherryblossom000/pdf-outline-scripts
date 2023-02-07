# python -m bin.2023.methods_12

from lib.maths_textbook import (
    ChapterAnswers as CA,
    ExercisesAnswer as EA,
    REVIEW as R,
)
from lib.private import add_maths_textbook_answer_outlines

# fmt: off
answers = [
    CA(1, [
        EA(1, "A", "D"),
        EA(2, "E", R)
    ]),
    CA(3, [
        EA(3, "A", "C"),
        EA(4, "D"),
        EA(5, "E", "G"),
        EA(6, "H", R)
    ]),
    CA(7, [
        EA(7, "A", "B"),
        EA(8, "C", "D"),
        EA(9, "E"),
        EA(10, "F"),
        EA(11, "G", "H"),
        EA(12, "I", "J"),
        EA(13, "K", "L"),
        EA(14, R)
    ]),
    CA(16, [
        EA(16, "A"),
        EA(17, "B"),
        EA(18, "C"),
        EA(19, "D", "E"),
        EA(21, "F", R)
    ]),
    CA(22, [
        EA(22, "A"),
        EA(23, "B"),
        EA(25, "C"),
        EA(26, "D", "E"),
        EA(27, "F"),
        EA(28, "G", "H"),
        EA(29, R)
    ]),
    CA(31, [
        EA(31, "A", "D"),
        EA(32, "E", "F"),
        EA(33, "G", "H"),
        EA(34, "I"),
        EA(35, "J", "K"),
        EA(36, R)
    ]),
    CA(37, [
        EA(37, "A"),
        EA(38, "B", "C"),
        EA(39, "D", "E"),
        EA(40, R)
    ]),
    CA(41, R),
    CA(43, [
        EA(43, "A", "C"),
        EA(44, "D", "F"),
        EA(45, "G", "I"),
        EA(46, R)
    ]),
    CA(47, [
        EA(47, "A", R)
    ]),
    CA(48, [
        EA(48, "A", "C"),
        EA(49, R)
    ]),
    CA(49, R),
    CA(50, [
        EA(50, "A", "C"),
        EA(51, "D", "F"),
        EA(52, "G", "H"),
        EA(53, R)
    ]),
    CA(54, [
        EA(54, "A", "D"),
        EA(55, "E", "F"),
        EA(57, "G", "H"),
        EA(58, "I"),
        EA(59, "J", "K"),
        EA(60, "L", R)
    ]),
    CA(61, R),
    CA(63, [
        EA(63, "A"),
        EA(64, "B", "D"),
        EA(65, "E", R)
    ]),
    CA(66, [
        EA(66, "A", "C"),
        EA(67, "D", "G"),
        EA(68, R)
    ]),
    CA(69, [
        EA(69, "A", "D"),
        EA(70, "E", "F"),
        EA(71, "G", R)
    ]),
    CA(73, R),
    CA(75, [
        EA(75, "A", "C"),
        EA(76, "D", R)
    ]),
    CA(77, [
        EA(77, "A", "C"),
        EA(78, R)
    ]),
    CA(79, R),
    CA(79, R),
    CA(81, [
        EA(81, 1),
        EA(82, 2),
        EA(83, 3)
    ])
]
# fmt: on

add_maths_textbook_answer_outlines(
    "Methods/1&2/Answers 2023 Cambridge Methods 1&2.pdf",
    answers,
)
