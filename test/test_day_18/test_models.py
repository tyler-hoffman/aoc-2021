import unittest
from parameterized import parameterized

from src.day_18.parser import Parser


SMALL_SAMPLE_A = """
[1,1]
[2,2]
[3,3]
[4,4]
"""

SMALL_SAMPLE_B = """
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
"""

SMALL_SAMPLE_C = """
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
"""

LARGER_SAMPLE = """
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
"""


class TestDay18SnailfishNumber(unittest.TestCase):
    @parameterized.expand(
        [
            ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
            ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
            ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
            (
                "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]",
                "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]",
            ),
            ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
        ]
    )
    def test_reduce_next(self, input: str, expected: str):
        snailfish_number = Parser.parse_snailfish_number(input)

        snailfish_number.reduce_next()

        self.assertEqual(str(snailfish_number), expected)

    @parameterized.expand(
        [
            (
                "[[[[4,3],4],4],[7,[[8,4],9]]]",
                "[1,1]",
                "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]",
            ),
            (
                "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
                "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
                "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]",
            ),
        ]
    )
    def test_add(self, a_str: str, b_str: str, expected_str: str):
        a = Parser.parse_snailfish_number(a_str)
        b = Parser.parse_snailfish_number(b_str)
        total = a + b
        expected = Parser.parse_snailfish_number(expected_str)
        self.assertEqual(total, expected)

    @parameterized.expand(
        [
            ("[[1,2],[[3,4],5]]", 143),
            ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
            ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
            ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
            ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
            ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
        ]
    )
    def test_magnitude(self, line: str, expected: int):
        snailfish_number = Parser.parse_snailfish_number(line)
        self.assertEqual(snailfish_number.magnitude, expected)
