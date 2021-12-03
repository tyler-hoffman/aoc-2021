import unittest

from src.day_03.b import C02ScrubberRatingFinder, OxygenGeneratorRatingFinder, solve
from src.day_03.shared import parse


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


class TestDay03B(unittest.TestCase):
    def test_oxygen(self):
        input = parse(SAMPLE_DATA)
        finder = OxygenGeneratorRatingFinder()
        self.assertEqual(finder.filter_lines(input), "10111")

    def test_co2(self):
        input = parse(SAMPLE_DATA)
        finder = C02ScrubberRatingFinder()
        self.assertEqual(finder.filter_lines(input), "01010")

    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 230)

    def test_solution(self):
        with open("src/day_03/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 5941884)
