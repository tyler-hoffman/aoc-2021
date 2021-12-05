import unittest

from .sample_data import SAMPLE_DATA
from src.day_04.b import solve


class TestDay04B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 1924)

    def test_solution(self):
        with open("src/day_04/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 2568)
