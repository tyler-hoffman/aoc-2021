import unittest

from .sample_data import SAMPLE_DATA
from src.day_23.b import solve


class TestDay23B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 44169)

    def test_solution(self):
        with open("src/day_23/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 53308)
