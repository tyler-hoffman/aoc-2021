import unittest

from src.day_02.b import solve_for_file, solve

SAMPLE_DATA = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


class TestDay02B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 900)

    def test_solution(self):
        with open("src/day_02/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve_for_file(), 2073416724)
