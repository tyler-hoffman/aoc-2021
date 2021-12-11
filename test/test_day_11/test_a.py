import unittest

from .sample_data import SAMPLE_DATA
from src.day_11.a import solve


class TestDay11A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 1656)

    def test_solve(self):
        with open("src/day_11/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 1743)
