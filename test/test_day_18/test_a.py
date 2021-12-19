import unittest
from parameterized import parameterized

from src.day_18.parser import Parser
from src.day_18.a import Day18PartASolver, solve
from test.test_day_18.sample_data import SAMPLE_DATA

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


class TestDay18A(unittest.TestCase):

    @parameterized.expand([
        ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
        ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
        ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
        ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
        ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
    ])
    def test_reduce_next(self, input: str, expected: str):
        snailfish_number = Parser(input).get_snailfish_number()

        snailfish_number.reduce_next()

        self.assertEqual(str(snailfish_number), expected)


    @parameterized.expand([
        ("[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]", "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"),
        ("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]", "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]", "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]"),
    ])
    def test_add(self, a_str: str, b_str: str, expected_str: str):
        a = Parser(a_str).get_snailfish_number()
        b = Parser(b_str).get_snailfish_number()
        total = a + b
        expected = Parser(expected_str).get_snailfish_number()
        self.assertEqual(total, expected)

    @parameterized.expand([
        (SMALL_SAMPLE_A, "[[[[1,1],[2,2]],[3,3]],[4,4]]"),
        (SMALL_SAMPLE_B, "[[[[3,0],[5,3]],[4,4]],[5,5]]"),
        (SMALL_SAMPLE_C, "[[[[5,0],[7,4]],[5,5]],[6,6]]"),
        (LARGER_SAMPLE, "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"),
    ])
    def test_solution_sum(self, input: str, expected: str):
        snailfish_numbers = Parser.parse(input)
        solution = Day18PartASolver(snailfish_numbers=snailfish_numbers)
        self.assertEqual(solution.sum, Parser(expected).get_snailfish_number())

    @parameterized.expand([
        ("[[1,2],[[3,4],5]]", 143),
        ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
        ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
        ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
        ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
        ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
    ])
    def test_magnitude(self, line: str, expected: int):
        snailfish_number = Parser(line).get_snailfish_number()
        self.assertEqual(snailfish_number.magnitude, expected)

    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 4140)

    def test_solution(self):
        with open("src/day_18/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 3574)
