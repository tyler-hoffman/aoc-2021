from functools import cache, cached_property
from itertools import product
from queue import PriorityQueue
from dataclasses import dataclass, field
from src.day_15.parser import Parser
from src.day_15.solver import Solver
from src.utils.point import Point


infinity = float("inf")


@dataclass
class Day15PartBSolver(Solver):
    grid: dict[Point, int]
    explored: dict[Point, int] = field(default_factory=dict)
    to_expand_queue: PriorityQueue[tuple[int, int, Point]] = field(
        default_factory=PriorityQueue
    )
    in_queue: dict[Point, int] = field(default_factory=dict)

    @property
    def solution(self) -> int:
        risk = 0
        point = Point(x=0, y=0)
        self.explore(point, 0)

        while point != self.end:
            risk, _, point = self.to_expand_queue.get()
            self.explore(point, risk)

        return risk

    def explore(self, point: Point, total_risk: int) -> None:
        self.explored[point] = total_risk
        for direction in self.directions:
            new_point = point + direction
            if new_point in self.grid and new_point not in self.explored:
                new_total_risk = self.grid[new_point] + total_risk
                if new_total_risk < self.in_queue.get(new_point, infinity):
                    self.to_expand_queue.put(
                        (new_total_risk, -new_point.magnitude, new_point)
                    )
                    self.in_queue[new_point] = new_total_risk

    @cached_property
    def directions(self) -> list[Point]:
        return [
            Point(x=-1, y=0),
            Point(x=1, y=0),
            Point(x=0, y=-1),
            Point(x=0, y=1),
        ]

    @cached_property
    def start(self) -> Point:
        return Point(x=0, y=0)

    @cached_property
    def end(self) -> Point:
        x_max = max([p.x for p in self.grid.keys()])
        y_max = max([p.y for p in self.grid.keys()])
        return Point(x=x_max, y=y_max)

def expanded(grid: dict[Point, int]) -> dict[Point, int]:
    block_width = max([p.x for p in grid.keys()]) + 1
    block_height = max([p.y for p in grid.keys()]) + 1

    output = dict[Point, int]()
    for x_block, y_block in product(range(0, 5), range(0, 5)):
        for point, risk in grid.items():
            new_point = point + Point(x=block_width * x_block, y=block_height * y_block)
            new_risk = increment(risk, x_block + y_block)
            output[new_point] = new_risk
    return output

@cache
def increment(num: int, amt: int) -> int:
    for _ in range(amt):
        num += 1
        if num == 10:
            num = 1
    return num


def solve(input: str) -> int:
    grid = Parser.parse(input)
    grid = expanded(grid)
    solver = Day15PartBSolver(grid=grid)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_15/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
