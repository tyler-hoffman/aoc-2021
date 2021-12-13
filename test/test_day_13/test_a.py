import unittest

from .sample_data import SAMPLE_DATA
from src.day_13.a import solve


class TestDay13A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 17)

    def test_solution(self):
        with open("src/day_13/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 775)
