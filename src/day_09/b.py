from functools import cached_property
from typing import List, Set
from queue import Queue
from src.day_09.parser import Parser
from src.day_09.solver import Solver
from src.utils.point import Point


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
    def basins(self) -> List[Set[Point]]:
        return [self.get_basin_for_point(point) for point in self.low_points]

    def get_basin_for_point(self, start: Point) -> Set[Point]:
        basin: Set[Point] = set([start])
        to_check: Queue[Point] = Queue()

        for n in self.neighbors(start):
            n_level = self.grid.value_at(n)
            if n_level > self.grid.value_at(start) and n_level < 9:
                to_check.put(n)

        while not to_check.empty():
            point = to_check.get()
            level = self.grid.value_at(point)
            neighbors = self.neighbors(point)
            lower_neighbors = [n for n in neighbors if self.grid.value_at(n) < level]
            all_lower_neighbors_are_in_basin = all(
                [n in basin for n in lower_neighbors]
            )
            if all_lower_neighbors_are_in_basin:
                basin.add((point))
                for n in neighbors:
                    neighbor_level = self.grid.value_at(n)
                    if neighbor_level > level and neighbor_level < 9:
                        to_check.put(n)

        return basin


def solve(input: str) -> int:
    parser = Parser()
    solver = Day09PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_09/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
