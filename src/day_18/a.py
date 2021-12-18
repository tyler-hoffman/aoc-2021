from dataclasses import dataclass
from src.day_18.parser import Parser
from src.day_18.solver import SnailfishNumber, Solver


@dataclass
class Day18PartASolver(Solver):
    snailfish_numbers: list[SnailfishNumber]

    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    snailfish_numbers = Parser.parse(input)
    solver = Day18PartASolver(snailfish_numbers=snailfish_numbers)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_18/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
