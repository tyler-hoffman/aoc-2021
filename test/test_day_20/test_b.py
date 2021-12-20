import unittest

from .sample_data import SAMPLE_DATA
from src.day_20.b import solve


class TestDay20B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 3351)

        with open("src/day_20/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 16112)
