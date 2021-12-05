import unittest

from .sample_data import SAMPLE_DATA
from src.day_01.a import solve


class TestDay01A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 7)

    def test_solution(self):
        with open("src/day_01/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 1228)
