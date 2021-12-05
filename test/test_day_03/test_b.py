import unittest

from .sample_data import SAMPLE_DATA
from src.day_03.b import C02ScrubberRatingFinder, OxygenGeneratorRatingFinder, solve
from src.day_03.shared import parse


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
