from dataclasses import dataclass

from src.day_02.parser import Parser
from src.day_02.solver import Solver
from src.utils.point import Point


@dataclass
class Day02BSolver(Solver):
    aim: int = 0

    def _up(self, value: int) -> Point:
        self.aim -= value

    def _down(self, value: int) -> Point:
        self.aim += value

    def _forward(self, value: int) -> Point:
        self.point += Point(x=value, y=value * self.aim)


def solve(input: str) -> int:
    solver = Day02BSolver(directions=Parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_02/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
