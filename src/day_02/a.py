from src.day_02.parser import Parser
from src.day_02.solver import Solver
from src.utils.point import Point


class Day02ASolver(Solver):
    def _up(self, value: int) -> Point:
        self.point += Point(x=0, y=-value)

    def _down(self, value: int) -> Point:
        self.point += Point(x=0, y=value)

    def _forward(self, value: int) -> Point:
        self.point += Point(x=value, y=0)


def solve(input: str) -> int:
    solver = Day02ASolver(directions=Parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_02/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
