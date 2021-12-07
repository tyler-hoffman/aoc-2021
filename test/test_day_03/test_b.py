import unittest

from src.day_03.parser import Parser

from .sample_data import SAMPLE_DATA
from src.day_03.b import C02ScrubberRatingFinder, OxygenGeneratorRatingFinder, solve


class TestDay03B(unittest.TestCase):
    def test_oxygen(self):
        lines = Parser.parse(SAMPLE_DATA)
        finder = OxygenGeneratorRatingFinder(lines=lines)
        self.assertEqual(finder.filtered_lines, "10111")

    def test_co2(self):
        lines = Parser.parse(SAMPLE_DATA)
        finder = C02ScrubberRatingFinder(lines=lines)
        self.assertEqual(finder.filtered_lines, "01010")

    def test_solve(self):
        self.assertEqual(solve(SAMPLE_DATA), 230)

    def test_solution(self):
        with open("src/day_03/input.txt", "r") as f:
            input = f.read()
        self.assertEqual(solve(input), 5941884)
