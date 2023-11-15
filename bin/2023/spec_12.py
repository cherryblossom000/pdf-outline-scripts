# python -m bin.2023.spec_12

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
		EA(2, "E", "H"),
		EA(3, "I", R)
	]),
	CA(4, [
		EA(4, "A", "C"),
		EA(5, "D", R)
	]),
	CA(6, [
		EA(6, "A", "B"),
		EA(7, "C", "E"),
		EA(8, "F", "H"),
		EA(9, R)
	]),
	CA(9, [
		EA(9, "A"),
		EA(10, "B", "D"),
		EA(11, "E", R)
	]),
	CA(12, R),
	# chapter 6: solutions supplement
	CA(14, R),
	CA(14, [
		EA(14, "A", "B"),
		EA(15, "C", "D"),
		EA(16, "E"),
		EA(17, "F"),
		EA(18, "G", R)
	]),
	CA(19, [
		EA(19, "A", "B"),
		EA(20, "C"),
		EA(21, "D"),
		EA(23, R)
	]),
	CA(24, [
		EA(24, "A", "C"),
		EA(24, "D", R)
	]),
	CA(26, R),
	CA(27, [
		EA(27, "A", "B"),
		EA(28, "C", "D"),
		EA(29, "E", R)
	]),
	CA(30, [
		EA(30, "A", "B"),
		EA(32, "C", "E"),
		EA(33, "F"),
		EA(34, "G", R)
	]),
	CA(35, R),
	CA(36, [
		EA(36, "A", "B"),
		EA(37, "C", R)
	]),
	CA(38, [
		EA(38, "A", "F"),
		EA(39, "G", R)
	]),
	CA(39, [
		EA(39, "A"),
		EA(40, "B", "D"),
		EA(41, R)
	]),
	CA(42, [
		EA(42, "A", "B"),
		EA(44, "C"),
		EA(46, "D"),
		EA(47, "E"),
		EA(48, "F", "G"),
		EA(49, "H"),
		EA(50, "I"),
		EA(51, "J", "K"),
		EA(52, R)
	]),
	CA(54, [
		EA(54, "A"),
		EA(55, "B", "D"),
		EA(56, "E", "G"),
		EA(58, R)
	]),
	CA(59, R),
	CA(63, [
		EA(63, "A"),
		EA(64, "B", "C"),
		EA(65, "D", "E"),
		EA(66, "F", "G"),
		EA(67, "H", R)
	]),
	CA(68, [
		EA(68, "A"),
		EA(69, "B"),
		EA(70, "C", "G"),
		EA(71, "H", R)
	]),
	CA(72, R),
	CA(74, [
		EA(74, "A", "D"),
		EA(75, R)
	])
]
# fmt: on

add_maths_textbook_answer_outlines(
	"Spec/1&2/Answers 2023 Cambridge Spec 1&2.pdf",
	answers,
)
