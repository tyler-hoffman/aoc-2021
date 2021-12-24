from src.day_23.parser import Parser
from src.day_23.solver import Solver


def solve(input: str) -> int:
    start_state = Parser.parse_with_folds(input)
    solver = Solver(start_state=start_state)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_23/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
