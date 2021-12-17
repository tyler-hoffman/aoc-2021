from src.day_17.parser import Parser
from src.day_17.solver import Solver

class Day17PartBSolver(Solver):
    @property
    def solution(self) -> int:
        return -1


def solve(input: str) -> int:
    parser = Parser()
    solver = Day17PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_17/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
