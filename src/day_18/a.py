from dataclasses import dataclass
from functools import cached_property
from src.day_18.parser import Parser
from src.day_18.solver import SnailfishNumber, Solver


@dataclass
class Day18PartASolver(Solver):
    snailfish_numbers: list[SnailfishNumber]

    @cached_property
    def solution(self) -> int:
        return self.sum.magnitude

    @cached_property
    def sum(self) -> SnailfishNumber:
        snailfish_number = self.snailfish_numbers[0]
        for x in self.snailfish_numbers[1:]:
            snailfish_number += x
        return snailfish_number


def solve(input: str) -> int:
    snailfish_numbers = Parser.parse(input)
    solver = Day18PartASolver(snailfish_numbers=snailfish_numbers)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_18/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
