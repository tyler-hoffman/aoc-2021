from src.day_07.parser import Parser
from src.day_07.solver import Solver


class Day07PartASolver(Solver):
    def move_cost(self, dist: int) -> int:
        return dist


def solve(input: str) -> int:
    parser = Parser()
    solver = Day07PartASolver(starting_positions=parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_07/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
