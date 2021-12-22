import unittest

from .sample_data import LARGER_DATA
from src.day_22.b import solve


class TestDay22B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(LARGER_DATA), 2758514936282235)

    def test_solution(self):
        with open("src/day_22/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 1165737675582132)
