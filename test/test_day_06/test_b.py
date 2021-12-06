import unittest

from .sample_data import SAMPLE_DATA
from src.day_06.b import solve


class TestDay06B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA, 256), 26984457539)

    def test_solution(self):
        with open("src/day_06/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input, 256), 1733403626279)
