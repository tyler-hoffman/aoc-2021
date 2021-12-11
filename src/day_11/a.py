from src.day_11.parser import Parser
from src.day_11.solver import Solver


class Day11PartASolver(Solver):
    @property
    def solution(self) -> int:
        for _ in range(100):
            self.do_step()

        return self.total_flashes


def solve(input: str) -> int:
    octopuses = Parser.parse(input)
    solver = Day11PartASolver(octopuses=octopuses)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_11/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
