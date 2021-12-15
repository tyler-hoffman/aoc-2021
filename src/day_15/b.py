from functools import cache, cached_property
from itertools import product
from dataclasses import dataclass
from src.day_15.parser import Parser
from src.day_15.solver import Solver
from src.utils.point import Point


@dataclass
class Day15PartBSolver(Solver):
    input_grid: dict[Point, int]

    @cached_property
    def grid(self) -> dict[Point, int]:
        block_width = max([p.x for p in self.input_grid.keys()]) + 1
        block_height = max([p.y for p in self.input_grid.keys()]) + 1

        output = dict[Point, int]()
        for x_block, y_block in product(range(0, 5), range(0, 5)):
            for point, risk in self.input_grid.items():
                new_point = point + Point(
                    x=block_width * x_block, y=block_height * y_block
                )
                new_risk = self.increment(risk, x_block + y_block)
                output[new_point] = new_risk
        return output

    @staticmethod
    @cache
    def increment(num: int, amt: int) -> int:
        for _ in range(amt):
            num += 1
            if num == 10:
                num = 1
        return num


def solve(input: str) -> int:
    grid = Parser.parse(input)
    solver = Day15PartBSolver(input_grid=grid)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_15/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
