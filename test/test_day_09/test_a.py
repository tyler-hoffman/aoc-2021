import unittest

from .sample_data import SAMPLE_DATA
from src.day_09.a import solve


class TestDay09A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 15)

    def test_solution(self):
        with open("src/day_09/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 452)
