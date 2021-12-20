from dataclasses import dataclass
from src.day_20.parser import Parser
from src.day_20.solver import Solver
from src.utils.point import Point


@dataclass
class Day20PartASolver(Solver):
    algorithm: list[bool]
    input_image: set[Point]

    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day20PartASolver(algorithm=data.algorithm, input_image=data.algorithm)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_20/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
