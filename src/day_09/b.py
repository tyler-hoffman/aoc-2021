from dataclasses import dataclass, field
from functools import cached_property
from typing import List, Set
from queue import Queue
from src.day_09.parser import Parser
from src.day_09.solver import Solver
from src.utils.point import Point


Basin = Set[Point]


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
    def basins(self) -> List[Basin]:
        return [
            BasinDiscoverer(start=point, grid=self.grid).basin
            for point in self.low_points
        ]


@dataclass
class BasinDiscoverer(object):
    grid: List[List[int]]
    start: Point
    discovered: Set[Point] = field(default_factory=set)
    to_check: Queue[Point] = Queue()

    @property
    def basin(self) -> Basin:
        self._add_point(self.start)

        while not self.to_check.empty():
            point = self.to_check.get()
            level = self.grid.value_at(point)
            neighbors = self.grid.neighbors(point)
            lower_neighbors = [n for n in neighbors if self.grid.value_at(n) < level]
            all_lower_neighbors_are_in_basin = all(
                [n in self.discovered for n in lower_neighbors]
            )
            if all_lower_neighbors_are_in_basin:
                self._add_point(point)

        return self.discovered

    def _add_point(self, point: Point) -> None:
        self.discovered.add(point)
        for n in self.grid.neighbors(point):
            level = self.grid.value_at(n)
            if level > self.grid.value_at(point) and level < 9:
                self.to_check.put(n)


def solve(input: str) -> int:
    parser = Parser()
    solver = Day09PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_09/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
