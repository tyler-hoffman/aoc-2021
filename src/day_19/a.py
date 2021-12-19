from dataclasses import dataclass
from functools import cached_property
from src.day_19.models import Point3D
from src.day_19.parser import Parser
from src.day_19.solver import Solver
from src.utils.collections import frequency_map


@dataclass
class Day19PartASolver(Solver):

    @cached_property
    def solution(self) -> int:
        self.group_them()

        points = set[Point3D]()
        for reading in self.grouped:
            for point in reading.points:
                points.add(point)
        return len(points)


def solve(input: str) -> int:
    scanner_readings = Parser.parse(input)
    solver = Day19PartASolver(scanner_readings=scanner_readings)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_19/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
