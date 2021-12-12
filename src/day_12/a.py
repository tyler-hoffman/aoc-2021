from src.day_12.parser import Parser
from src.day_12.solver import PathFinder, Solver


def solve(input: str) -> int:
    cave_system = Parser.parse(input)
    path_finder = PathFinder(cave_system=cave_system)
    solver = Solver(path_finder=path_finder)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_12/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
