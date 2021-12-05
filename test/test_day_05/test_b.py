import unittest

from src.day_05.b import solve


SAMPLE_DATA = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


class TestDay05B(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 12)

    def test_solution(self):
        with open("src/day_05/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 21514)
