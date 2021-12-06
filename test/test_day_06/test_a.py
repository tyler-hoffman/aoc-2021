import unittest

from parameterized import parameterized
from .sample_data import SAMPLE_DATA
from src.day_06.a import solve


class TestDay06A(unittest.TestCase):
    @parameterized.expand([
        (18, 26),
        (80, 5934),
    ])
    def test_solve(self, days: int, expected: int):
        self.assertEqual(solve(SAMPLE_DATA, days), expected)

    def test_solution(self):
        with open("src/day_06/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input, 80), 386640)
