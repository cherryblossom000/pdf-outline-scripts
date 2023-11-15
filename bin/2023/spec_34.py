# python -m bin.2023.spec_34

from lib.maths_textbook import (
	ChapterAnswers as CA,
	ExercisesAnswer as EA,
	REVIEW as R,
)
from lib.private import add_maths_textbook_answer_outlines

# fmt: off
answers = [
	CA(1, [
		EA(1, "A"),
		EA(2, "B", "C"),
		EA(3, "D"),
		EA(4, "E"),
		EA(6, "F"),
		EA(8, "G"),
		EA(9, "H"),
		EA(10, R)
	]),
	# Chapter 2: see solutions supplement
	CA(12, R),
	CA(12, [
		EA(12, "A"),
		EA(13, "B"),
		EA(14, "C"),
		EA(15, "D"),
		EA(16, "E", R)
	]),
	CA(19, [
		EA(19, "A"),
		EA(20, "B"),
		EA(21, "C", "E"),
		EA(22, "F", R)
	]),
	CA(23, [
		EA(23, "A"),
		EA(24, "B", "E"),
		EA(25, R)
	]),
	CA(25, [
		EA(25, "A", "B"),
		EA(26, "C", "E"),
		EA(27, "F", "G"),
		EA(28, "H"),
		EA(30, R)
	]),
	CA(33, R),
	CA(37, [
		EA(37, "A"),
		EA(38, "B", "C"),
		EA(39, "D"),
		EA(40, "E", "F"),
		EA(41, "G"),
		EA(44, "H", "I"),
		EA(45, R)
	]),
	CA(48, [
		EA(48, "A"),
		EA(49, "B", "E"),
		EA(50, "F", "G"),
		EA(51, "H", "I"),
		EA(52, R)
	]),
	CA(53, [
		EA(53, "A"),
		EA(54, "B"),
		EA(56, "C", "D"),
		EA(57, "E", "F"),
		EA(58, R)
	]),
	CA(60, [
		EA(60, "A", "C"),
		EA(61, "D"),
		EA(62, "E"),
		EA(63, "F", "I"),
		EA(64, "J", R)
	]),
	CA(66,[
		EA(66, "A"),
		EA(67, "B", "C"),
		EA(68, "D", R)
	]),
	CA(70, [
		EA(70, "A"),
		EA(71, "B"),
		EA(73, "C"),
		EA(74, "D"),
		EA(74, R)
	]),
	CA(76, R),
	CA(81, [
		EA(81, "A", "E"),
		EA(82, "F", R)
	]),
	CA(82, [
		EA(82, "A", "B"),
		EA(83, "C", R)
	]),
	CA(84, R),
	CA(85, R)
]
# fmt: on

add_maths_textbook_answer_outlines(
	"Spec/3&4/Answers 2023 Cambridge Spec 3&4.pdf",
	answers,
)
