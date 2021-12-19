from src.day_19.parser import Parser
from src.day_19.solver import Solver

class Day19PartASolver(Solver):
    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    parser = Parser()
    solver = Day19PartASolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_19/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
