from dataclasses import dataclass
from src.day_12.models import CaveSystem
from src.day_12.parser import Parser
from src.day_12.solver import PathFinder, Solver


@dataclass
class Day12PartASolver(Solver):
    cave_system: CaveSystem

    @property
    def solution(self) -> int:
        count = 0
        path_finder = PathFinder(cave_system=self.cave_system)
        paths = []
        for path in path_finder.get_paths():
            paths.append(path)
            count += 1
        return count


def solve(input: str) -> int:
    cave_system = Parser.parse(input)
    solver = Day12PartASolver(cave_system=cave_system)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_12/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
