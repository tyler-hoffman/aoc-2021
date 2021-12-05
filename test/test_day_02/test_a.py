import unittest

from .sample_data import SAMPLE_DATA
from src.day_02.a import solve


class TestDay02A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 150)

    def test_solution(self):
        with open("src/day_02/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 2117664)
