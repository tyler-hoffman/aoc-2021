from src.day_06.parser import Parser
from src.day_06.solver import Solver


def solve(input: str, days: int) -> int:
    parser = Parser()
    solver = Solver(parser.parse(input), days)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_06/input.txt", "r") as f:
        input = f.read()
    print(solve(input, 80))
