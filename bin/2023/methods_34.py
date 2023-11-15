# python -m bin.2023.methods_34

from lib.maths_textbook import (
	ChapterAnswers as CA,
	ExercisesAnswer as EA,
	REVIEW as R,
)
from lib.private import add_maths_textbook_answer_outlines

# fmt: off
answers = [
	CA(1, [
		EA(1, "A", "B"),
		EA(3, "C"),
		EA(4, "D"),
		EA(5, "E", "F"),
		EA(8, "G", "H"),
		EA(9, R)
	]),
	CA(10, [
		EA(10, "A"),
		EA(11, "B", "C"),
		EA(12, "D", R)
	]),
	CA(13, [
		EA(13, "A"),
		EA(15, "B"),
		EA(16, "C", "D"),
		EA(17, "E", "F"),
		EA(20, "G"),
		EA(21, "H", "I"),
		EA(22, R)
	]),
	CA(24, [
		EA(24, "A"),
		EA(27, "B", "D"),
		EA(28, "E", "F"),
		EA(29, "G"),
		EA(30, "H", R)
	]),
	CA(33, [
		EA(33, "A"),
		EA(35, "B"),
		EA(37, "C", "E"),
		EA(39, "F", "G"),
		EA(40, "H", "I"),
		EA(41, R)
	]),
	CA(42, [
		EA(42, "A", "B"),
		EA(43, "C", "D"),
		EA(44, "E"),
		EA(45, "F"),
		EA(46, "G"),
		EA(48, "H"),
		EA(49, "I", "J"),
		EA(51, "K", "L"),
		EA(52, R)
	]),
	CA(54, [
		EA(54, "A"),
		EA(55, "B", "C"),
		EA(56, "D", R)
	]),
	CA(58, R),
	CA(61, [
		EA(61, "A", "D"),
		EA(63, "E", "G"),
		EA(64, "H", "K"),
		EA(65, "L", R)
	]),
	CA(66, [
		EA(66, "A"),
		EA(67, "B", "C"),
		EA(68, "D"),
		EA(71, "E"),
		EA(72, "F", "G"),
		EA(73, "H", R)
	]),
	CA(78, [
		EA(78, "A", "D"),
		EA(79, "E", "F"),
		EA(80, "G"),
		EA(81, "H", "I"),
		EA(82, "J", R)
	]),
	CA(84, R),
	CA(86, [
		EA(86, "A", "C"),
		EA(88, "D", R)
	]),
	CA(89, [
		EA(89, "A", R)
	]),
	CA(90, [
		EA(90, "A", "B"),
		EA(91, "C", R)
	]),
	CA(92, [
		EA(92, "A", "B"),
		EA(93, "C", R)
	]),
	CA(94, [
		EA(94, "A", "C"),
		EA(95, "D", R)
	]),
	CA(95, R),
	CA(96, R),
	CA(102, [
		EA(102, 1, 2),
		EA(103, 3)
	], "B")
]
# fmt: on

add_maths_textbook_answer_outlines(
	"Methods/3&4/Answers 2023 Cambridge Methods 3&4.pdf",
	answers,
)
