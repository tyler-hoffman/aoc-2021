from functools import cached_property
from src.day_11.parser import Parser
from src.day_11.solver import Solver


class Day11PartBSolver(Solver):
    @property
    def solution(self) -> int:
        while True:
            flashes = self.do_step()
            if flashes == self.target_flashes:
                return self.steps_completed

    @cached_property
    def target_flashes(self) -> int:
        return len(self.octopuses)


def solve(input: str) -> int:
    parser = Parser()
    solver = Day11PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_11/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
