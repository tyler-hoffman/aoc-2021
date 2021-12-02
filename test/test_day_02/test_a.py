import unittest

from src.day_02.a import solve_for_file, solve


SAMPLE_DATA = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


class TestDay02A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 150)

    def test_solution(self):
        self.assertEqual(solve_for_file(), 2117664)
