import unittest

from src.day_01.a import solve


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
        input = open("src/day_01/input.txt", "r").read()
        self.assertEqual(solve(input), 1228)
