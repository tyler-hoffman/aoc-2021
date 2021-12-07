import unittest

from .sample_data import SAMPLE_DATA
from src.day_07.a import solve


class TestDay07A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 37)

    def test_solution(self):
        with open("src/day_07/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 335330)
