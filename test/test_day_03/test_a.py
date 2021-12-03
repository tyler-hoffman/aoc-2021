import unittest

from src.day_03.a import solve


SAMPLE_DATA = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


class TestDay03A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 198)

    def test_solution(self):
        with open("src/day_03/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 4006064)
