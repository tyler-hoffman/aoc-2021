from dataclasses import dataclass
from typing import List
from src.day_06.parser import Parser
from src.day_06.solver import Solver

@dataclass
class Day06PartASolver(Solver):

    @property
    def solution(self) -> int:
        days_passed = 0
        for freq in self._frequencies_at_days():
            days_passed += 1
            if days_passed == self.days:
                return sum(freq.values())


def solve(input: str, days: int) -> int:
    parser = Parser()
    solver = Day06PartASolver(parser.parse(input), days)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_06/input.txt", "r") as f:
        input = f.read()
    print(solve(input, 80))
