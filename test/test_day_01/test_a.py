import unittest

from src.day_01.a import solve_for_file, solve


SAMPLE_INPUT = """
199
200
208
210
200
207
240
269
260
263
"""


class TestDay01A(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(SAMPLE_INPUT), 7)

    def test_solution(self):
        with open("src/day_01/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve_for_file(), 1228)
