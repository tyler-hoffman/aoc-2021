import unittest

from .sample_data import SAMPLE_DATA
from src.day_10.b import solve


class TestDay10B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 288957)

    def test_solution(self):
        with open("src/day_10/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 3354640192)
