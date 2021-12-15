from functools import cached_property
from dataclasses import dataclass
from src.day_15.parser import Parser
from src.day_15.solver import Solver
from src.utils.point import Point


@dataclass
class Day15PartASolver(Solver):
    input_grid: dict[Point, int]

    @cached_property
    def grid(self) -> dict[Point, int]:
        return self.input_grid


def solve(input: str) -> int:
    grid = Parser.parse(input)
    solver = Day15PartASolver(input_grid=grid)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_15/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
