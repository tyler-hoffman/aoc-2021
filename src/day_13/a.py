from src.day_13.parser import Parser
from src.day_13.solver import Solver

class Day13PartASolver(Solver):
    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    parser = Parser()
    solver = Day13PartASolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_13/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
