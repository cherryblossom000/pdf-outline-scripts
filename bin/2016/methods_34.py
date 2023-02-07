# python -m bin.2016.methods_34

from lib.maths_textbook import (
    Chapter as C,
    ChapterAnswers as CA,
    Exercise as E,
    ExercisesAnswer as EA,
    ExercisesChapter as EC,
    RevisionChapter as RC,
    REVIEW as R,
)
from lib.private import VCEUnits, add_maths_textbook_outlines

# fmt: off
chapters = [
    C(13, EC("Functions and relations", [
        E(14, "Set notation and sets of numbers", 17),
        E(18, "Identifying and describing relations and functions", 25),
        E(27, "Types of functions and implied domains", 32),
        E(36, "Sums and products of functions", 38),
        E(40, "Composite functions", 43),
        E(44, "Inverse functions", 51),
        E(55, "Power functions", 61),
        E(62, "Applications of functions", 64)
    ], 66)),
    C(75, EC("Coordinate geometry and matrices", [
        E(76, "Linear equations", 76),
        E(78, "Linear literal equations and simultaneous linear literal equations", 79),
        E(80, "Linear coordinate geometry", 83),
        E(86, "Applications of linear functions", 86),
        E(88, "Matrices", 94),
        E(95, "The geometry of simultaneous linear equations with two variables", 97),
        E(98, "Simultaneous linear equations with more than two variables", 101)
    ], 103)),
    C(109, EC("Transformations", [
        E(110, "Translations", 113),
        E(115, "Dilations", 119),
        E(120, "Reflections", 122),
        E(123, "Combinations of transformations", 127),
        E(129, "Determining transformations", 131),
        E(132, "Using transformations to sketch graphs", 134),
        E(135, "Transformations of power functions with positive integer index", 140),
        E(141, "Determining the rule for a function from its graph", 142),
        E(143, "Using matrices for transformations", 149),
        E(151, "Using the inverse of a 2 × 2 matrix for transformations", 153)
    ], 155)),
    C(162, EC("Polynomial functions", [
        E(163, "Quadratic functions", 171),
        E(173, "Determining the rule for a parabola", 176),
        E(178, "The language of polynomials", 182),
        E(183, "Division and factorisation of polynomials", 191),
        E(194, "The general cubic function", 198),
        E(198, "Polynomials of higher degree", 201),
        E(201, "Determining the rule for the graph of a polynomial", 206),
        E(208, "Solution of literal equations and systems of equations", 211)
    ], 213)),
    C(221, EC("Exponential and logarithmic functions", [
        E(222, "Exponential functions", 227),
        E(228, "The exponential function f(x) = eˣ", 230),
        E(232, "Exponential equations", 233),
        E(234, "Logarithms", 239),
        E(241, "Graphing logarithmic functions", 244),
        E(245, "Determining rules for graphs of exponential and logarithmic functions", 247),
        E(248, "Solution of exponential equations using logarithms", 250),
        E(251, "Inverses", 253),
        E(255, "Exponential growth and decay", 258)
    ], 260)),
    C(266, EC("Circular functions", [
        E(267, "Measuring angles in degrees and radians", 268),
        E(269, "Defining circular functions: sine, cosine and tangent", 275),
        E(276, "Further symmetry properties and the Pythagorean identity", 277),
        E(278, "Graphs of sine and cosine", 283),
        E(284, "Solution of trigonometric equations", 288),
        E(289, "Sketch graphs of y = a sin n(t ± ε) and y = a cos n(t ± ε)", 291),
        E(292, "Sketch graphs of y = a sin n(t ± ε) ± b and y = a cos n(t±ε) ± b", 293),
        E(295, "Addition of ordinates for circular functions", 295),
        E(296, "Determining rules for graphs of circular functions", 297),
        E(299, "The tangent function", 304),
        E(306, "General solution of trigonometric equations", 309),
        E(310, "Applications of circular functions", 312)
    ], 314)),
    C(323, EC("Further functions", [
        E(324, "More power functions", 326),
        E(327, "Composite and inverse functions", 330),
        E(332, "Sums and products of functions and addition of ordinates", 333),
        E(334, "Function notation and identities", 335),
        E(336, "Families of functions and solving literal equations", 338)
    ], 341)),
    C(345, RC(347, 357)),
    C(362, EC("Differentiation", [
        E(363, "The derivative", 368),
        E(369, "Rules for differentiation", 376),
        E(379, "Differentiating xⁿ where n is a negative integer", 381),
        E(382, "The graph of the derivative function", 385),
        E(387, "The chain rule", 390),
        E(391, "Differentiating rational powers", 394),
        E(394, "Differentiation of eˣ", 397),
        E(398, "Differentiation of the natural logarithm function", 400),
        E(400, "Derivatives of circular functions", 404),
        E(405, "The product rule", 408),
        E(409, "The quotient rule", 411),
        E(412, "Limits and continuity", 418),
        E(419, "When is a function differentiable?", 420)
    ], 422)),
    C(428, EC("Applications of differentiation", [
        E(429, "Tangents and normals", 432),
        E(434, "Rates of change", 437),
        E(440, "Stationary points", 443),
        E(444, "Types of stationary points", 450),
        E(454, "Absolute maximum and minimum values", 456),
        E(457, "Maximum and minimum problems", 466),
        E(469, "Families of functions", 470)
    ], 472)),
    C(489, EC("Integration", [
        E(490, "The area under a graph", 494),
        E(496, "Antidifferentiation: indefinite integrals", 499),
        E(500, "The antiderivative of (ax + b)ʳ", 505),
        E(506, "The antiderivative of eᵏˣ", 507),
        E(507, "The fundamental theorem of calculus and the definite integral", 511),
        E(511, "Finding the area under a curve", 514),
        E(515, "Integration of circular functions", 517),
        E(518, "Miscellaneous exercises", 520),
        E(523, "The area of a region between two curves", 526),
        E(528, "Applications of integration", 531),
        E(535, "The fundamental theorem of calculus")
    ], 538)),
    C(547, RC(550, 558)),
    C(562, EC("Discrete random variables and their probability distributions", [
        E(563, "Sample spaces and probability", 570),
        E(573, "Conditional probability and independence", 578),
        E(581, "Discrete random variables", 585),
        E(588, "Expected value (mean), variance and standard deviation", 596)
    ], 600)),
    C(608, EC("The binomial distribution", [
        E(609, "Bernoulli sequences and the binomial probability distribution", 614),
        E(616, "The graph, expectation and variance of a binomial distribution", 619),
        E(620, "Finding the sample size", 623),
        E(624, "Proofs for the expectation and variance")
    ], 626)),
    C(631, EC("Continuous random variables and their probability distributions", [
        E(632, "Continuous random variables", 640),
        E(642, "Mean and median for a continuous random variable", 647),
        E(650, "Measures of spread", 652),
        E(654, "Properties of mean and variance*", 565),
        E(657, "Cumulative distribution functions*", 658)
    ], 659)),
    C(666, EC("The normal distribution", [
        E(667, "The normal distribution", 671),
        E(673, "Standardisation and the 68–95–99.7% rule", 676),
        E(678, "Determining normal probabilities", 682),
        E(684, "Solving problems using the normal distribution", 687),
        E(689, "The normal approximation to the binomial distribution", 691)
    ], 692)),
    C(698, EC("Sampling and estimation", [
        E(699, "Populations and samples", 704),
        E(706, "The exact distribution of the sample proportion", 712),
        E(714, "Approximating the distribution of the sample proportion", 718),
        E(720, "Confidence intervals for the population proportion", 727)
    ], 729)),
    C(735, RC(737, 742)),
    C(748, RC(751, 755)),
    C(771, EC("Counting methods and the binomial theorem", [
        E(771, "Counting methods", 773),
        E(744, "Summation notation", 775),
        E(775, "The binomial theorem", 777)
    ]))
]

answers = [
    CA(786, [
        EA(786, "A", "B"),
        EA(788, "C"),
        EA(789, "D"),
        EA(790, "E", "F"),
        EA(793, "G", "H"),
        EA(794, R)
    ]),
    CA(795, [
        EA(795, "A"),
        EA(796, "B", "C"),
        EA(797, "D", "G"),
        EA(798, R)
    ]),
    CA(798, [
        EA(798, "A"),
        EA(800, "B"),
        EA(801, "C", "D"),
        EA(802, "E", "F"),
        EA(805, "G"),
        EA(806, "H", "J"),
        EA(807, R)
    ]),
    CA(809, [
        EA(809, "A"),
        EA(811, "B", "C"),
        EA(812, "D", "E"),
        EA(813, "F"),
        EA(814, "G", "H"),
        EA(815, R)
    ]),
    CA(817, [
        EA(817, "A"),
        EA(820, "B"),
        EA(821, "C", "E"),
        EA(823, "F", "G"),
        EA(824, "H"),
        EA(825, "I", R)
    ]),
    CA(826, [
        EA(826, "A", "B"),
        EA(827, "C", "D"),
        EA(828, "E", "F"),
        EA(829, "G"),
        EA(832, "H", "I"),
        EA(833, "J"),
        EA(834, "K"),
        EA(835, "L", R)
    ]),
    CA(837, [
        EA(837, "A"),
        EA(838, "B"),
        EA(839, "C", "E"),
        EA(840, R)
    ]),
    CA(841, R),
    CA(843, [
        EA(843, "A", "B"),
        EA(844, "C", "D"),
        EA(846, "E", "H"),
        EA(847, "I", "L"),
        EA(848, "M", R)
    ]),
    CA(849, [
        EA(849, "A"),
        EA(850, "B", "D"),
        EA(854, "E", "F"),
        EA(855, "G"),
        EA(856, R)
    ]),
    CA(860, [
        EA(860, "A", "B"),
        EA(861, "C", "F"),
        EA(862, "G"),
        EA(863, "H"),
        EA(864, "I", "J"),
        EA(865, R)
    ]),
    CA(866, R),
    CA(868, [
        EA(868, "A", "B"),
        EA(869, "C"),
        EA(870, "D", R)
    ]),
    CA(871, [
        EA(871, "A", "C"),
        EA(872, R)
    ]),
    CA(872, [
        EA(872, "A"),
        EA(873, "B", R)
    ]),
    CA(874, [
        EA(874, "A", "B"),
        EA(875, "C", R)
    ]),
    CA(876, [
        EA(876, "A", "C"),
        EA(877, "D", R)
    ]),
    CA(877, R),
    CA(878, R),
    CA(884, [
        EA(884, 1, 3)
    ])
]
# fmt: on

add_maths_textbook_outlines(
    name="Mathematical Methods",
    subject="Maths Methods",
    units=VCEUnits.three_four,
    introduction=8,
    acknowledgments=9,
    overview=10,
    glossary=778,
    chapters=chapters,
    answers=answers,
)
