from src.day_15.parser import Parser
from src.day_15.solver import Solver

class Day15PartASolver(Solver):
    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    parser = Parser()
    solver = Day15PartASolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_15/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
