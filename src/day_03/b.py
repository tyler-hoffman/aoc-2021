from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import List

from src.day_03.parser import Parser
from src.day_03.solver import LineAnalyzer, Solver


@dataclass
class RatingFinder(ABC):
    lines: List[str]

    @abstractmethod
    def select_winning_bit(self, zero_count, one_count: int) -> str:
        ...

    @property
    def rating(self) -> int:
        rating_string = self.filtered_lines
        return int(rating_string, 2)

    @property
    def filtered_lines(self) -> str:
        lines = self.lines.copy()
        for index in range(len(lines[0])):
            line_analyzer = LineAnalyzer(lines)
            if line_analyzer.line_count == 1:
                break
            zero_count, one_count = line_analyzer.zeros_and_ones_for_position(index)
            winning_bit = self.select_winning_bit(
                zero_count=zero_count, one_count=one_count
            )

            lines = [line for line in lines if line[index] == winning_bit]

        assert len(lines) == 1
        return lines[0]


class OxygenGeneratorRatingFinder(RatingFinder):
    def select_winning_bit(self, zero_count, one_count: int) -> str:
        return "1" if one_count >= zero_count else "0"


class C02ScrubberRatingFinder(RatingFinder):
    def select_winning_bit(self, zero_count, one_count: int) -> str:
        return "0" if zero_count <= one_count else "1"


class Day03BSolver(Solver):
    @property
    def solution(self):
        o2_finder = OxygenGeneratorRatingFinder(self.lines)
        c02_finder = C02ScrubberRatingFinder(self.lines)

        return o2_finder.rating * c02_finder.rating


def solve(input: str) -> int:
    solver = Day03BSolver(lines=Parser.parse(input))
    return solver.solution


if __name__ == "__main__":
    with open("src/day_03/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
