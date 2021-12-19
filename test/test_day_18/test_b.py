import unittest

from .sample_data import SAMPLE_DATA
from src.day_18.b import solve


class TestDay18B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 3993)

    def test_solution(self):
        with open("src/day_18/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 4763)
