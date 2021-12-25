import unittest

from .sample_data import SAMPLE_DATA
from src.day_25.a import solve


class TestDay25A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 58)

    def test_solution(self):
        with open("src/day_25/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 300)
