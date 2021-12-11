from dataclasses import dataclass
from functools import cached_property
from itertools import product

from src.day_11.models import OctopusCluster
from src.day_11.parser import Parser
from src.day_11.solver import Solver
from src.utils.point import Point


@dataclass
class Day11PartASolver(Solver):
    octopuses: OctopusCluster
    total_flashes: int = 0

    @property
    def solution(self) -> int:
        for _ in range(100):
            self.do_step()

        return self.total_flashes

    def do_step(self) -> None:
        to_flash = self.increment_all_and_return_flashed()
        flashed: list[Point] = []

        while len(to_flash):
            point = to_flash.pop()
            to_flash += self.increment_neighbors_and_return_flashed(point)
            flashed.append(point)
            self.total_flashes += 1

        self.reset_points(flashed)

    def increment_all_and_return_flashed(self) -> list[Point]:
        flashed: list[Point] = []
        for point in self.octopuses:
            self.octopuses[point] += 1
            if self.octopuses[point] == 10:
                flashed.append(point)
        return flashed

    def increment_neighbors_and_return_flashed(self, point: Point) -> list[Point]:
        to_flash: list[Point] = []
        for neighbor in self.neighbors_of(point):
            self.octopuses[neighbor] += 1
            if self.octopuses[neighbor] == 10:
                to_flash.append(neighbor)

        return to_flash


    def reset_points(self, points: list[Point]) -> None:
        for point in points:
            self.octopuses[point] = 0

    def neighbors_of(self, point: Point) -> set[Point]:
        potential_neighbors = {point + neighbor for neighbor in self.neighbor_differences}
        return {point for point in potential_neighbors if point in self.octopuses}

    @cached_property
    def neighbor_differences(self) -> set[Point]:
        diffs = [-1, 0, 1]

        return {Point(x=x ,y=y) for x, y in product(diffs, diffs) if x or y}


def solve(input: str) -> int:
    octopuses = Parser.parse(input)
    solver = Day11PartASolver(octopuses=octopuses)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_11/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
