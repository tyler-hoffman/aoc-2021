from dataclasses import dataclass
from typing import List, Optional
from src.day_08.models import Entry
from src.day_08.parser import Parser
from src.day_08.solver import NumberInfo, Solver


@dataclass
class Day08PartASolver(Solver):
    entries: List[Entry]

    @property
    def solution(self) -> int:
        count = 0
        for entry in self.entries:
            for digit in entry.output_value:
                if NumberInfo.is_unique_length(len(digit)):
                    count += 1
        return count


def solve(input: str) -> int:
    entries = Parser.parse(input)
    solver = Day08PartASolver(entries=entries)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_08/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
