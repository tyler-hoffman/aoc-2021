from functools import cached_property
from typing import List, Set, Tuple
from queue import Queue
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
        return [self.get_basin_for_point(x, y) for x, y in self.low_points]

    def get_basin_for_point(self, x: int, y: int) -> List[Tuple[int, int]]:
        so_far: Set[Tuple[int, int]] = set([(x, y)])
        to_check: Queue[Tuple[int, int]] = Queue()
        for n in self.neighbors(x, y):
            n_level = self.grid.value_at(*n)
            if n_level > self.grid.value_at(x, y):
                to_check.put(n)

        while not to_check.empty():
            new_point = to_check.get()
            new_x, new_y = new_point
            level = self.grid.value_at(new_x, new_y)
            neighbors = self.neighbors(new_x, new_y)
            # Maybe remove equality????
            lower_neighbors = [n for n in neighbors if self.grid.value_at(*n) < level]
            all_lower_neighbors_are_in_basin = all([n in so_far for n in lower_neighbors])
            if level < 9 and all_lower_neighbors_are_in_basin:
                so_far.add((new_point))
                for n in neighbors:
                    neighbor_level = self.grid.value_at(*n)
                    if neighbor_level > level:
                        to_check.put(n)

        return so_far





def solve(input: str) -> int:
    parser = Parser()
    solver = Day09PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_09/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
