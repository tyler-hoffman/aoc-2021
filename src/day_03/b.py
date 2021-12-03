from abc import ABC, abstractmethod
from typing import Dict, List

from src.day_03.shared import parse
from src.utils.collections import frequency_map


def solve(input: str) -> int:
    lines = parse(input)

    o2_rating = OxygenGeneratorRatingFinder().find_rating(lines)
    c02_rating = C02ScrubberRatingFinder().find_rating(lines)

    return o2_rating * c02_rating


class RatingFinder(ABC):
    def find_rating(self, lines: List[str]) -> int:
        rating_string = self.filter_lines(lines)
        return int(rating_string, 2)

    def filter_lines(self, lines: List[str]) -> str:
        line_len = len(lines[0])
        winning_bit: str = ""
        for index in range(line_len):
            if len(lines) == 1:
                break

            freqs = frequency_map([line[index] for line in lines])
            zero_count = freqs.get("0", 0)
            one_count = freqs.get("1", 0)
            winning_bit = self.select_winning_bit(
                zero_count=zero_count, one_count=one_count
            )

            lines = [line for line in lines if line[index] == winning_bit]

        assert len(lines) == 1
        return lines[0]

    @abstractmethod
    def select_winning_bit(self, zero_count, one_count: int) -> str:
        ...


class OxygenGeneratorRatingFinder(RatingFinder):
    def select_winning_bit(self, zero_count, one_count: int) -> str:
        return "1" if one_count >= zero_count else "0"


class C02ScrubberRatingFinder(RatingFinder):
    def select_winning_bit(self, zero_count, one_count: int) -> str:
        return "0" if zero_count <= one_count else "1"


if __name__ == "__main__":
    with open("src/day_03/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
