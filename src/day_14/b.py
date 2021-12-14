from src.day_14.parser import Parser
from src.day_14.solver import Solver


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Solver(template=data.template, rules=data.rules, iterations=40)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_14/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
