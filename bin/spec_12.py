# python -m bin.spec_12

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
    C(15, EC("Algebra I", [
        E(16, "Indices", 17),
        E(19, "standard form", 21),
        E(22, "Solving linear equations and simultaneous linear equations", 26),
        E(27, "Solving problems with linear equations", 29),
        E(31, "Solving problems with simultaneous linear equations", 32),
        E(33, "Substitution and transposition of formulas", 34),
        E(36, "Algebraic fractions", 38),
        E(39, "Literal equations", 41),
        E(42, "Using a CAS calculator for algebra", 46)
    ], 47)),
    C(53, EC("Number systems and sets", [
        E(54, "Set notation", 56),
        E(57, "Sets of numbers", 61),
        E(62, "The modulus function", 64),
        E(65, "Surds", 70),
        E(71, "Natural numbers", 75),
        E(76, "Linear Diophantine equations", 79),
        E(80, "The Euclidean algorithm", 83),
        E(84, "Problems involving sets", 85)
    ], 88)),
    C(96, EC("Variation", [
        E(97, "Direct variation", 100),
        E(101, "Inverse variation", 104),
        E(105, "Fitting data", 109),
        E(112, "Joint variation", 113),
        E(115, "Part variation", 117)
    ], 118)),
    C(124, EC("Sequences and series", [
        E(125, "Introduction to sequences", 130),
        E(132, "Arithmetic sequences", 134),
        E(136, "Arithmetic series", 139),
        E(141, "Geometric sequences", 145),
        E(147, "Geometric series", 149),
        E(151, "Zeno’s paradox and infinite geometric series", 152)
    ], 154)),
    C(160, EC("Algebra II", [
        E(161, "Polynomial identities", 164),
        E(165, "Quadratic equations", 170),
        E(171, "Applying quadratic equations to rate problems", 174),
        E(176, "Partial fractions", 182),
        E(183, "Simultaneous equations", 185)
    ], 187)),
    C(191, RC(193, 196)),
    C(204, EC("Principles of counting", [
        E(205, "Basic counting methods", 207),
        E(209, "Factorial notation and permutations", 214),
        E(215, "Permutations with restrictions", 217),
        E(218, "Permutations of like objects", 220),
        E(221, "Combinations", 224),
        E(226, "Combinations with restrictions", 228),
        E(230, "Pascal’s triangle", 232),
        E(233, "The pigeonhole principle", 235),
        E(237, "The inclusion–exclusion principle", 240)
    ], 242)),
    C(246, EC("Number and proof", [
        E(247, "Direct proof", 250),
        E(252, "Proof by contrapositive", 255),
        E(256, "Proof by contradiction", 259),
        E(260, "Equivalent statements", 262),
        E(263, "Disproving statements", 264),
        E(265, "Mathematical induction", 272)
    ], 274)),
    C(279, EC("Geometry in the plane and proof", [
        E(280, "Points, lines and angles", 284),
        E(286, "Triangles and polygons", 289),
        E(291, "Congruence and proofs", 294),
        E(296, "Pythagoras’ theorem", 298),
        E(300, "Ratios", 300),
        E(302, "An introduction to similarity", 305),
        E(309, "Proofs involving similarity", 310),
        E(311, "Areas, volumes and similarity", 314),
        E(318, "The golden ratio", 321)
    ], 322)),
    C(330, EC("Circle geometry", [
        E(331, "Angle properties of the circle", 335),
        E(336, "Tangents", 339),
        E(340, "Chords in circles", 342)
    ], 343)),
    C(348, RC(351, 356)),
    C(361, EC("Sampling and sampling distributions", [
        E(362, "Populations and samples", 366),
        E(367, "The distribution of the sample proportion", 377),
        E(380, "Investigating the distribution of the sample proportion using simulation", 385),
        E(387, "Investigating the distribution of the sample mean using simulation", 393)
    ], 395)),
    C(401, EC("Trigonometric ratios and applications", [
        E(402, "Reviewing trigonometry", 404),
        E(407, "The sine rule", 409),
        E(411, "The cosine rule", 413),
        E(414, "The area of a triangle", 416),
        E(417, "Circle mensuration", 421),
        E(422, "Angles of elevation, angles of depression and bearings", 425),
        E(426, "Problems in three dimensions", 428),
        E(430, "Angles between planes and more difficult 3D problems", 433)
    ], 435)),
    C(441, EC("Further trigonometry", [
        E(442, "Symmetry properties", 443),
        E(444, "The tangent function", 447),
        E(447, "Reciprocal functions and the Pythagorean identity", 451),
        E(452, "Addition formulas and double angle formulas", 457),
        E(459, "Simplifying a cos x + b sin x", 461),
    ], 462)),
    C(467, EC("Graphing techniques", [
        E(468, "Reciprocal functions", 472),
        E(473, "Locus of points", 475),
        E(476, "Parabolas", 479),
        E(479, "Ellipses", 482),
        E(483, "Hyperbolas", 488),
        E(488, "Parametric equations", 495),
        E(497, "Polar coordinates", 499),
        E(499, "Graphing using polar coordinates", 501),
        E(502, "Further graphing using polar coordinates", 506)
    ], 507)),
    C(512, EC("Complex numbers", [
        E(513, "Starting to build the complex numbers", 516),
        E(517, "Multiplication and division of complex numbers", 522),
        E(523, "Argand diagrams", 526),
        E(527, "Solving equations over the complex numbers", 528),
        E(529, "Polar form of a complex number", 533)
    ], 534)),
    C(538, RC(540, 545)),
    C(549, EC("Matrices", [
        E(550, "Matrix notation", 552),
        E(554, "Addition, subtraction and multiplication by a real number", 557),
        E(558, "Multiplication of matrices", 560),
        E(561, "Identities, inverses and determinants for 2 × 2 matrices", 565),
        E(566, "Solution of simultaneous equations using matrices", 568)
    ], 569)),
    C(574, EC("Transformations of the plane", [
        E(575, "Linear transformations", 578),
        E(579, "Geometric transformations", 584),
        E(585, "Rotations and general reflections", 587),
        E(588, "Composition of transformations", 590),
        E(591, "Inverse transformations", 594),
        E(595, "Transformations of straight lines and other graphs", 598),
        E(599, "Area and determinant", 602),
        E(604, "General transformations", 606)
    ], 607)),
    C(612, EC("Vectors", [
        E(613, "Introduction to vectors", 619),
        E(621, "Components of vectors", 623),
        E(625, "Scalar product of vectors", 627),
        E(628, "Vector projections", 630),
        E(632, "Geometric proofs", 633),
        E(635, "Vectors in three dimensions", 637)
    ], 638)),
    C(643, RC(645, 649)),
    C(654, EC("Kinematics", [
        E(655, "Position, velocity and acceleration", 659),
        E(660, "Applications of antidifferentiation to kinematics", 663),
        E(664, "Constant acceleration", 666),
        E(667, "Velocity-time graphs", 671)
    ], 673)),
    C(680, EC("Statics of a particle", [
        E(681, "Forces and triangle of forces", 684),
        E(686, "Resolution of forces", 688)
    ], 690)),
    C(693, RC(695, 697))
]

answers = [
    CA(712, [
        EA(712, "A", "C"),
        EA(713, "D", "G"),
        EA(714, "H", R)
    ]),
    CA(715, [
        EA(715, "A"),
        EA(716, "B", "D"),
        EA(717, "E", "H"),
        EA(718, R)
    ]),
    CA(719, [
        EA(719, "A", "C"),
        EA(720, "D", R)
    ]),
    CA(721, [
        EA(721, "A", "C"),
        EA(722, "D", R)
    ]),
    CA(723, [
        EA(723, "A", "B"),
        EA(724, "C", "E"),
        EA(725, R)
    ]),
    CA(725, R),
    CA(727, [
        EA(727, "A", "D"),
        EA(728, "E", "H"),
        EA(729, "I", R)
    ]),
    # TODO: check solutions supplement for chapter 8
    CA(729, R),
    CA(729, [
        EA(729, "A"),
        EA(730, "B", "H"),
        EA(731, "I", R)
    ]),
    CA(731, [
        EA(731, "A", "B"),
        EA(732, "C", R)
    ]),
    CA(732, R),
    CA(732, [
        EA(732, "A"),
        EA(733, "B", "D"),
        EA(734, R)
    ]),
    CA(734, [
        EA(734, "A", "C"),
        EA(735, "D", R)
    ]),
    CA(736, [
        EA(736, "A", "B"),
        EA(737, "C", "E"),
        EA(738, R)
    ]),
    CA(739, [
        EA(739, "A"),
        EA(741, "B", "D"),
        EA(742, "E"),
        EA(743, "F"),
        EA(744, "G", "I"),
        EA(745, R)
    ]),
    CA(746, [
        EA(746, "A"),
        EA(747, "B", "E"),
        EA(748, R)
    ]),
    CA(749, R),
    CA(751, [
        EA(751, "A", "B"),
        EA(752, "C", "D"),
        EA(753, "E", R)
    ]),
    CA(753, [
        EA(753, "A"),
        EA(754, "B"),
        EA(755, "C", "D"),
        EA(756, "E", "G"),
        EA(757, "H", R)
    ]),
    CA(759, [
        EA(759, "A"),
        EA(760, "B", "D"),
        EA(761, "E", R)
    ]),
    CA(762, R),
    CA(764, [
        EA(764, "A", "D"),
        EA(765, R)
    ]),
    CA(766, [
        EA(766, "A", R)
    ]),
    CA(766, R)
]
# fmt: on

add_maths_textbook_outlines(
    name="Specialist Mathematics",
    subject="Specialist Maths",
    units=VCEUnits.one_two,
    introduction=9,
    acknowledgments=11,
    overview=12,
    glossary=699,
    chapters=chapters,
    answers=answers,
    final_revision=False,
)
