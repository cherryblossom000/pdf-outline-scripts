# python -m bin.2023.chem_12

from lib.lib import OutlineNode as O, add_outlines
from lib.private import tutoring_get_paths


def real_page_numbers(outline: O) -> O:
	return O(
		outline.page + 16, outline.label, list(map(real_page_numbers, outline.children))
	)


# fmt: off
outlines = [
	O(3, "About the authors"),
	O(7, "Overview: How to use this resource"),
	O(12, "Overview: Aboriginal and Torres Strait Islander knowledge, cultures and history"),
	O(13, "Concept maps for Units 1 & 2"),
	O(17, "Acknowledgements"),
] + list(map(real_page_numbers, (
	O(2, "Unit 1 How can the diversity of materials be explained?", [
		O(2, "Chapter 1 Elements and the periodic table", [
			O(7, "1A Introduction to the elements"),
			O(14, "1B Electron configurations"),
			O(26, "1C The periodic table"),
			O(41, "1D Critical elements and recycling processes"),
			O(57, "Chapter 1 review"),
		]),
		O(62, "Chapter 2 Covalent substances", [
			O(66, "2A Representing covalent compounds"),
			O(74, "2B Molecular shapes and polarity"),
			O(81, "2C Properties of covalent compounds determined by intermolecular forces"),
			O(89, "2D Diamond and graphite as covalent compounds"),
			O(95, "Chapter 2 review"),
		]),
		O(98, "Chapter 3 Metals", [
			O(101, "3A Structure and properties of metals"),
			O(106, "3B Reactivity of metals"),
			O(113, "3C Metal recycling"),
			O(119, "Chapter 3 review"),
		]),
		O(122, "Chapter 4 Ionic compounds", [
			O(126, "4A Formation and naming of ionic compounds"),
			O(138, "4B Structure and properties of ionic compounds"),
			O(145, "4C Precipitation reactions"),
			O(154, "Chapter 4 review"),
		]),
		O(158, "Chapter 5 Separating and identifying compounds in mixtures", [
			O(161, "5A Polarity"),
			O(168, "5B Chromatography"),
			O(175, "Chapter 5 review"),
		]),
		O(180, "Chapter 6 Quantifying atoms and compounds", [
			O(183, "6A Relative atomic and isotopic masses"),
			O(190, "6B The mole"),
			O(195, "6C Percentage composition and empirical formula"),
			O(201, "Chapter 6 review"),
		]),
		O(204, "Chapter 7 Organic compounds", [
			O(208, "7A Organic chemistry in society"),
			O(218, "7B Hydrocarbons"),
			O(238, "7C Haloalkanes"),
			O(248, "7D Alcohols and carboxylic acids"),
			O(261, "Chapter 7 review"),
		]),
		O(266, "Chapter 8 Polymers", [
			O(269, "8A Polymerisation reactions"),
			O(276, "8B Polymer recycling"),
			O(283, "Chapter 8 review"),
		]),
		O(286, "Chapter 9 Research investigations", [
			O(290, "9A Preparing a research investigation"),
			O(301, "9B Thinking organisers"),
			O(308, "9C Broader considerations on chemistry"),
			O(323, "Chapter 9 review"),
		]),
		O(327, "Unit 1 Revision exercise"),
	]),
	O(334, "Unit 2 How do chemical reactions shape the natural world?", [
		O(334, "Chapter 10 Water and properties of water", [
			O(337, "10A Water on Earth"),
			O(342, "10B Properties of water"),
			O(351, "Chapter 10 review"),
		]),
		O(354, "Chapter 11 Acids and bases", [
			O(358, "11A Introduction to acids and bases"),
			O(366, "11B Strong and weak acids and bases"),
			O(372, "11C Calculating pH"),
			O(387, "11D Carbon dioxide as a weak acid"),
			O(393, "11E Neutralisation reactions"),
			O(402, "Chapter 11 review"),
		]),
		O(408, "Chapter 12 Redox reactions", [
			O(411, "12A Reduction and oxidation"),
			O(422, "12B Writing redox equations"),
			O(429, "12C Metal displacement reactions"),
			O(433, "12D Applications of redox reactions in society"),
			O(442, "Chapter 12 review"),
		]),
		O(446, "Chapter 13 Measuring solubility and concentration", [
			O(449, "13A Measures of solubility"),
			O(456, "13B Predicting solubility"),
			O(461, "13C Purifying water"),
			O(468, "13D Volumetric analysis of acids and bases"),
			O(478, "Chapter 13 review"),
		]),
		O(482, "Chapter 14 Analysis of salts in water", [
			O(485, "14A Sources of salt in water"),
			O(495, "14B Gravimetric analysis of salts"),
			O(508, "14C Determining salt concentration using spectroscopy"),
			O(520, "Chapter 14 review"),
		]),
		O(524, "Chapter 15 Gases", [
			O(527, "15A Gases and the ideal gas equation"),
			O(533, "15B Gas stoichiometry and the greenhouse effect"),
			O(544, "Chapter 15 review"),
		]),
		O(548, "Chapter 16 Practical investigations", [
			O(552, "16A Investigative planning and design"),
			O(564, "16B Scientific evidence"),
			O(576, "16C Scientific communication"),
			O(578, "Chapter 16 review"),
		]),
		O(586, "Unit 2 Revision exercise"),
		O(592, "Glossary"),
		O(604, "Appendix: Periodic table"),
		O(605, "Index"),
		O(512, "Permissions acknowledgements"),
	]),
)))

(input, output) = tutoring_get_paths(
	"Chem/1&2/2023 Cambridge Chem 1&2.pdf"
)
add_outlines(input, output, outlines)
