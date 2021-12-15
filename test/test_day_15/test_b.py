import unittest

from .sample_data import SAMPLE_DATA
from src.day_15.b import solve


class TestDay15B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 315)

    def test_solution(self):
        with open("src/day_15/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 2914)
