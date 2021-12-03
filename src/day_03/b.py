from abc import ABC, abstractmethod
from typing import Dict, List

from src.day_03.shared import parse
from src.utils.collections import frequency_map


def solve(input: str) -> int:
    lines = parse(input)

    oxygen_generator_rating = OxygenGeneratorRatingFinder().filter_lines(lines)
    c02_scrubber_rating = C02ScrubberRatingFinder().filter_lines(lines)

    return int(oxygen_generator_rating, 2) * int(c02_scrubber_rating, 2)


class RatingFinder(ABC):
    def filter_lines(self, lines: List[str]) -> str:
        line_len = len(lines[0])
        winning_bit: str = ""
        for index in range(line_len):
            if len(lines) == 1:
                break
            freqs = frequency_map([line[index] for line in lines])
            winning_bit = self.select_winning_bit(freqs)

            lines = [line for line in lines if line[index] == winning_bit]

        assert len(lines) == 1
        return lines[0]

    @abstractmethod
    def select_winning_bit(freqs: Dict[str, int]) -> str:
        ...


class OxygenGeneratorRatingFinder(RatingFinder):
    def select_winning_bit(self, freqs: Dict[str, int]) -> str:
        zero_count = freqs.get("0", 0)
        one_count = freqs.get("1", 0)

        return "1" if one_count >= zero_count else "0"


class C02ScrubberRatingFinder(RatingFinder):
    def select_winning_bit(self, freqs: Dict[str, int]) -> str:
        zero_count = freqs.get("0", 0)
        one_count = freqs.get("1", 0)

        return "0" if zero_count <= one_count else "1"


if __name__ == "__main__":
    with open("src/day_03/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
