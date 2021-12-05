import unittest

from .sample_data import SAMPLE_DATA
from src.day_04.a import solve


class TestDay04A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 4512)

    def test_solution(self):
        with open("src/day_04/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 45031)
