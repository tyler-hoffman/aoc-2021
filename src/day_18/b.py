from dataclasses import dataclass
from functools import cached_property
from itertools import permutations
from src.day_18.parser import Parser
from src.day_18.solver import SnailfishNumber


@dataclass
class Day18PartBSolver(object):
    snailfish_numbers: list[SnailfishNumber]

    @cached_property
    def solution(self) -> int:
        return max(self.possible_magnitudes)

    @cached_property
    def possible_magnitudes(self) -> set[int]:
        pairs = permutations(self.snailfish_numbers, 2)
        sums = [a + b for a, b in pairs]
        return {x.magnitude for x in sums}


def solve(input: str) -> int:
    snailfish_numbers = Parser.parse_all(input)
    solver = Day18PartBSolver(snailfish_numbers=snailfish_numbers)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_18/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
