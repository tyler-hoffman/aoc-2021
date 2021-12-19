from functools import cached_property
from itertools import combinations
from src.day_19.parser import Parser
from src.day_19.solver import Solver


class Day19PartBSolver(Solver):
    @cached_property
    def solution(self) -> int:
        max_dist = 0
        for a, b in combinations(self.oriented_scanners, 2):
            dist = a.position.manhattan_dist(b.position)
            if dist > max_dist:
                max_dist = dist
        return max_dist


def solve(input: str) -> int:
    scanner_readings = Parser.parse(input)
    solver = Day19PartBSolver(scanner_readings=scanner_readings)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_19/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
