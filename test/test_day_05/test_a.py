import unittest

from .sample_data import SAMPLE_DATA
from src.day_05.a import solve


class TestDay05A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 5)

    def test_solution(self):
        with open("src/day_05/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 5373)
