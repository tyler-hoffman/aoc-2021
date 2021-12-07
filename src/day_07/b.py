from functools import cached_property
from typing import Dict
from src.day_07.parser import Parser
from src.day_07.solver import Solver


class Day07PartBSolver(Solver):
    @cached_property
    def cost_map(self) -> Dict[int, int]:
        output = [0]
        for i in range(1, self.max_pos - self.min_pos + 1):
            output.append(i + output[i - 1])
        return output

    def move_cost(self, dist: int) -> int:
        return self.cost_map[dist]


def solve(input: str) -> int:
    parser = Parser()
    solver = Day07PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_07/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
