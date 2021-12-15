import unittest

from .sample_data import SAMPLE_DATA
from src.day_15.a import solve


class TestDay15A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 40)

    def test_solution(self):
        with open("src/day_15/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 595)
