from src.day_09.parser import Parser
from src.day_09.solver import Solver


class Day09PartASolver(Solver):
    @property
    def solution(self) -> int:
        risk_levels = [self.risk_level(self.grid.value_at(point)) for point in self.low_points]
        return sum(risk_levels)

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
