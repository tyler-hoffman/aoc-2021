import unittest

from .sample_data import SAMPLE_DATA
from src.day_19.b import solve


class TestDay19B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 3621)

    def test_solution(self):
        with open("src/day_19/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 12092)
