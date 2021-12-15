from abc import ABC, abstractmethod
from functools import cached_property
from queue import PriorityQueue

from src.utils.point import Point


infinity = float("inf")


class Solver(ABC):
    @property
    @abstractmethod
    def grid(self) -> dict[Point, int]:
        ...

    @property
    def solution(self) -> int:
        risk = 0
        point = Point(x=0, y=0)
        self.explore(point, 0)

        while point != self.end:
            _, risk, point = self.to_expand_queue.get()
            self.explore(point, risk)

        return risk

    def explore(self, point: Point, total_risk: int) -> None:
        self.explored[point] = total_risk
        for direction in self.directions:
            new_point = point + direction
            new_total_risk = total_risk + self.grid.get(new_point, infinity)
            if all(
                [
                    new_point in self.grid,
                    new_point not in self.explored,
                    new_total_risk < self.in_queue.get(new_point, infinity),
                ]
            ):
                optimistic_cost = new_point.manhattan_dist(self.end) + new_total_risk
                self.to_expand_queue.put((optimistic_cost, new_total_risk, new_point))
                self.in_queue[new_point] = new_total_risk

    @cached_property
    def explored(self) -> dict[Point, int]:
        return dict()

    @cached_property
    def to_expand_queue(self) -> PriorityQueue[tuple[int, int, Point]]:
        return PriorityQueue()

    @cached_property
    def in_queue(self) -> dict[Point, int]:
        return dict()

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
