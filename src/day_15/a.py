from functools import cached_property
from queue import PriorityQueue
from dataclasses import dataclass, field
from src.day_15.parser import Parser
from src.day_15.solver import Solver
from src.utils.point import Point


infinity = float("inf")


@dataclass
class Day15PartASolver(Solver):
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


def solve(input: str) -> int:
    grid = Parser.parse(input)
    solver = Day15PartASolver(grid=grid)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_15/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
