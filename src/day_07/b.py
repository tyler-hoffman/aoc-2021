from functools import cached_property
from typing import List
from src.day_07.parser import Parser
from src.day_07.solver import Solver


class Day07PartBSolver(Solver):
    @cached_property
    def move_costs(self) -> List[int]:
        output = [0]
        for i in range(1, self.max_pos - self.min_pos + 1):
            output.append(i + output[i - 1])
        return output

    def move_cost(self, dist: int) -> int:
        return self.move_costs[dist]


def solve(input: str) -> int:
    parser = Parser()
    solver = Day07PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_07/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
