import unittest

from .sample_data import SAMPLE_DATA
from src.day_17.a import solve


class TestDay17A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 45)

    def test_solution(self):
        with open("src/day_17/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 4005)
