import unittest

from .sample_data import SAMPLE_DATA
from src.day_08.b import solve


class TestDay08B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 61229)

    def test_solution(self):
        with open("src/day_08/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 1028926)