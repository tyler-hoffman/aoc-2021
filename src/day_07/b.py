from functools import cache
from src.day_07.parser import Parser
from src.day_07.solver import Solver


class Day07PartBSolver(Solver):

    @staticmethod
    @cache
    def move_cost(dist: int) -> int:
        if dist == 0:
            return 0
        else:
            return dist + Day07PartBSolver.move_cost(dist - 1)


def solve(input: str) -> int:
    parser = Parser()
    solver = Day07PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_07/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
