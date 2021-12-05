import unittest

from .sample_data import SAMPLE_DATA
from src.day_03.a import solve


class TestDay03A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 198)

    def test_solution(self):
        with open("src/day_03/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 4006064)
