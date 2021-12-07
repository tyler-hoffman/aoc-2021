from abc import abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import List

from src.day_02.models import Direction, Down, Forward, Up
from src.utils.point import Point


@dataclass
class Solver(object):
    directions: List[Direction]
    point = Point(x=0, y=0)

    @cached_property
    def solution(self) -> int:
        self.follow_directions()

        return self.point.x * self.point.y

    def follow_directions(self) -> Point:
        for direction in self.directions:
            match direction:
                case Up(value=value):
                    self._up(value)
                case Down(value=value):
                    self._down(value)
                case Forward(value=value):
                    self._forward(value)
                case _:
                    raise Exception(f"Unknown direction: {direction}")

    @abstractmethod
    def _up(self, value: int) -> None:
        ...

    @abstractmethod
    def _down(self, value: int) -> None:
        ...

    @abstractmethod
    def _forward(self, value: int) -> None:
        ...
