import unittest
from parameterized import parameterized

from .sample_data import LARGE_DATA, SMALL_DATA
from src.day_22.a import solve


class TestDay22A(unittest.TestCase):
    @parameterized.expand(
        [
            (SMALL_DATA, 39),
            (LARGE_DATA, 590784),
        ]
    )
    def test_solve(self, input: str, expected: int):
        self.assertEqual(solve(input), expected)

    def test_solution(self):
        with open("src/day_22/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 551693)
