from typing import List
from src.day_09.parser import Parser
from src.day_09.solver import Solver


class Day09PartASolver(Solver):
    @property
    def solution(self) -> int:
        return sum(self.risk_level(p) for p in self.low_points)

    @property
    def low_points(self) -> List[int]:
        points: List[int] = []
        for y in range(self.grid.height):
            for x, level in enumerate(self.grid.levels[y]):
                if all([level < n for n in self.neighbors(x, y)]):
                    points.append(level)
        return points

    def neighbors(self, x: int, y: int) -> List[int]:
        output: List[int] = []
        if y > 0:
            output.append(self.grid.levels[y - 1][x])
        if y < self.grid.height - 1:
            output.append(self.grid.levels[y + 1][x])
        if x > 0:
            output.append(self.grid.levels[y][x - 1])
        if x < self.grid.width - 1:
            output.append(self.grid.levels[y][x + 1])
        return output

    def risk_level(self, height: int) -> int:
        return height + 1


def solve(input: str) -> int:
    parser = Parser()
    solver = Day09PartASolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_09/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
