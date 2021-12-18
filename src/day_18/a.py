from src.day_18.parser import Parser
from src.day_18.solver import Solver

class Day18PartASolver(Solver):
    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    parser = Parser()
    solver = Day18PartASolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_18/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
