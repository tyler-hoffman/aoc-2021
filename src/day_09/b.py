from functools import cached_property
from typing import List, Tuple
from src.day_09.parser import Parser
from src.day_09.solver import Solver


class Day09PartBSolver(Solver):
    @property
    def solution(self) -> int:
        sorted_basin_sizes = sorted(self.basin_sizes)
        a, b, c = sorted_basin_sizes[-3:]
        return a * b * c

    @cached_property
    def basin_sizes(self) -> List[int]:
        return [len(basin) for basin in self.basins]

    @cached_property
    def basins(self) -> List[List[Tuple[int, int]]]:
        [self.get_basin_for_point(x, y) for x, y in self.low_points]

    def get_basin_for_point(self, x: int, y: int): List[Tuple[int, int]]:
        pass


def solve(input: str) -> int:
    parser = Parser()
    solver = Day09PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_09/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
