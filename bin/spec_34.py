# python -m bin.spec_34

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
    C(13, EC("Preliminary topics", [
        E(14, "Circular functions", 23),
        E(26, "The sine and cosine rules", 30),
        E(31, "Geometry prerequisites", 33),
        E(35, "Sequences and series", 42),
        E(43, "The modulus function", 47),
        E(48, "Circles", 49),
        E(50, "Ellipses and hyperbolas", 56),
        E(57, "Parametric equations", 63)
    ], 69)),
    C(79, EC("Vectors", [
        E(80, "Introduction to vectors", 88),
        E(91, "Resolution of a vector into rectangular components", 98),
        E(103, "Scalar product of vectors", 106),
        E(108, "Vector projections", 110),
        E(111, "Collinearity", 113),
        E(114, "Geometric proofs", 117)
    ], 120)),
    C(130, EC("Circular functions", [
        E(131, "The reciprocal circular functions", 137),
        E(138, "Compound and double angle formulas", 143),
        E(145, "Inverses of circular functions", 150),
        E(152, "Solution of equations", 156),
    ], 159)),
    C(167, EC("Complex numbers", [
        E(168, "Starting to build the complex numbers", 175),
        E(176, "Modulus, conjugate and division", 180),
        E(181, "The modulus-argument form of a complex number", 185),
        E(186, "Basic operations on complex numbers in modulus-argument form", 190),
        E(192, "Solving quadratic equations over the complex numbers", 195),
        E(196, "Solving polynomial equations over the complex numbers", 201),
        E(203, "Using De Moivre’s theorem to solve equations", 205),
        E(206, "Sketching subsets of the complex plane", 209),
    ], 210)),
    C(218, RC(220, 229)),
    C(236, EC("Differentiation and rational functions", [
        E(237, "Differentiation", 241),
        E(242, "Derivatives of x = f(y)", 245),
        E(246, "Derivatives of inverse circular functions", 249),
        E(251, "Second derivatives", 253),
        E(253, "Points of inflection", 263),
        E(266, "Related rates", 271),
        E(274, "Rational functions", 281),
        E(283, "A summary of differentiation", 284),
        E(285, "Implicit differentiation", 289)
    ], 291)),
    C(300, EC("Techniques of integration", [
        E(301, "Antidifferentiation", 306),
        E(309, "Antiderivatives involving inverse circular functions", 310),
        E(311, "Integration by substitution", 316),
        E(317, "Definite integrals by substitution", 318),
        E(319, "Use of trigonometric identities for integration", 320),
        E(321, "Further substitution*", 323),
        E(324, "Partial fractions", 330),
        E(332, "Further techniques and miscellaneous exercises", 333),
    ], 336)),
    C(340, EC("Applications of integration", [
        E(341, "The fundamental theorem of calculus", 345),
        E(347, "Area of a region between two curves", 351),
        E(354, "Integration using a CAS calculator", 358),
        E(360, "Volumes of solids of revolution", 364),
        E(368, "Lengths of curves in the plane", 371)
    ], 372)),
    C(381, EC("Differential equations", [
        E(382, "An introduction to differential equations", 384),
        E(386, "Differential equations involving a function of the independent variable", 392),
        E(394, "Differential equations involving a function of the dependent variable", 396),
        E(396, "Applications of differential equations", 403),
        E(407, "Separation of variables", 410),
        E(411, "Differential equations with related rates", 414),
        E(416, "Using a definite integral to solve a differential equation", 417),
        E(418, "Using Euler’s method to solve a differential equation", 424),
        E(425, "Slope field for a differential equation", 427)
    ], 428)),
    C(437, EC("Kinematics", [
        E(438, "Position, velocity and acceleration", 450),
        E(453, "Constant acceleration", 456),
        E(458, "Velocity-time graphs", 462),
        E(465, "Differential equations of the form v = f(x) and a = f(v)", 467),
        E(469, "Other expressions for acceleration", 473)
    ], 474)),
    C(483, RC(485, 499)),
    C(506, EC("Vector functions", [
        E(507, "Vector functions", 510),
        E(511, "Position vectors as a function of time", 515),
        E(517, "Vector calculus", 522),
        E(523, "Velocity and acceleration for motion along a curve", 528)
    ], 531)),
    C(538, EC("Dynamics", [
        E(539, "Force", 544),
        E(548, "Newton’s laws of motion", 555),
        E(557, "Resolution of forces and inclined planes", 560),
        E(563, "Connected particles", 565),
        E(568, "Variable forces", 569),
        E(571, "Equilibrium", 575),
        E(577, "Vector functions", 579)
    ], 581)),
    C(589, RC(592, 598)),
    C(604, EC("Linear combinations of random variables and distribution of sample means", [
        E(605, "Linear combinations of random variables", 611),
        E(613, "Linear combinations of independent normal random variables", 614),
        E(615, "Simulating the distribution of sample means", 620),
        E(620, "The distribution of the sample mean of a normally distributed random variable", 624),
        E(626, "The central limit theorem", 631),
        E(632, "Confidence intervals for the population mean", 637)
    ], 640)),
    C(647, EC("Hypothesis testing for the mean", [
        E(648, "Hypothesis testing for the mean", 655),
        E(657, "One-tail and two-tail tests", 662),
        E(664, "Two-tail tests revisited", 666),
        E(668, "Errors in hypothesis testing", 669)
    ], 670)),
    C(676, RC(678, 680)),
    C(682, RC(684, 689)),
]

answers = [
    CA(706, [
        EA(706, "A"),
        EA(707, "B", "C"),
        EA(708, "D", "E"),
        EA(709, "F"),
        EA(711, "G"),
        EA(713, "H"),
        EA(714, "I", R)
    ]),
    CA(716, [
        EA(716, "A", "B"),
        EA(717, "C"),
        EA(718, "D", "F"),
        EA(719, R)
    ]),
    CA(720, [
        EA(720, "A"),
        EA(722, "B", "C"),
        EA(723, "D"),
        EA(724, R)
    ]),
    CA(727, [
        EA(727, "A", "D"),
        EA(728, "E", "F"),
        EA(729, "G"),
        EA(730, "H"),
        EA(732, R)
    ]),
    CA(735, R),
    CA(737, [
        EA(737, "A"),
        EA(738, "B", "C"),
        EA(740, "D", "E"),
        EA(741, "F", "G"),
        EA(744, "H"),
        EA(745, "I", R)
    ]),
    CA(748, [
        EA(748, "A"),
        EA(749, "B", "E"),
        EA(750, "F", "G"),
        EA(751, "H"),
        EA(752, R)
    ]),
    CA(752, [
        EA(752, "A"),
        EA(753, "B"),
        EA(755, "C"),
        EA(756, "D", "E"),
        EA(757, R)
    ]),
    CA(759, [
        EA(759, "A", "B"),
        EA(760, "C", "D"),
        EA(761, "E", "F"),
        EA(762, "G", "I"),
        EA(763, R)
    ]),
    CA(764, [
        EA(764, "A"),
        EA(765, "B", "C"),
        EA(766, "D", R)
    ]),
    CA(769, R),
    CA(772, [
        EA(772, "A"),
        EA(773, "B"),
        EA(775, "C"),
        EA(776, "D"),
        EA(777, R)
    ]),
    CA(778, [
        EA(778, "A", "B"),
        EA(779, "C", "E"),
        EA(780, "F", R)
    ]),
    CA(781, R),
    CA(783, [
        EA(783, "A", "F"),
        EA(784, R)
    ]),
    CA(784, [
        EA(784, "A", "B"),
        EA(785, "C", R)
    ]),
    CA(786, R),
    CA(787, R)
]
# fmt: on

add_maths_textbook_outlines(
    name="Specialist Mathematics",
    subject="Specialist Maths",
    units=VCEUnits.three_four,
    introduction=8,
    acknowledgments=9,
    overview=10,
    glossary=696,
    chapters=chapters,
    answers=answers,
)
