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
    @parameterized.expand(
        [
            (SMALL_SAMPLE_A, "[[[[1,1],[2,2]],[3,3]],[4,4]]"),
            (SMALL_SAMPLE_B, "[[[[3,0],[5,3]],[4,4]],[5,5]]"),
            (SMALL_SAMPLE_C, "[[[[5,0],[7,4]],[5,5]],[6,6]]"),
            (LARGER_SAMPLE, "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"),
        ]
    )
    def test_solution_sum(self, input: str, expected: str):
        snailfish_numbers = Parser.parse_all(input)
        solution = Day18PartASolver(snailfish_numbers=snailfish_numbers)
        self.assertEqual(solution.sum, Parser.parse_snailfish_number(expected))

    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 4140)

    def test_solution(self):
        with open("src/day_18/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 3574)
