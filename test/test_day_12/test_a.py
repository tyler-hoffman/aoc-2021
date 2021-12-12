import unittest

from parameterized import parameterized

from .sample_data import SAMPLE_DATA_A, SAMPLE_DATA_B, SAMPLE_DATA_C
from src.day_12.a import solve


class TestDay12A(unittest.TestCase):
    @parameterized.expand(
        [
            (SAMPLE_DATA_A, 10),
            (SAMPLE_DATA_B, 19),
            (SAMPLE_DATA_C, 226),
        ]
    )
    def test_solve(self, input: str, expected: int):
        self.assertEqual(solve(input), expected)

    def test_solution(self):
        with open("src/day_12/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 3713)
