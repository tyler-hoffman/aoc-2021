from dataclasses import dataclass
from more_itertools import nth
from typing import Iterator


@dataclass
class TargetArea(object):
    x_min: int
    x_max: int
    y_min: int
    y_max: int

@dataclass
class Trajectory(object):
    x_vel: int = 0
    y_vel: int = 0

    def x_at(self, t: int) -> int:
        return nth(self.x_points(), t)

    def y_at(self, t: int) -> int:
        return nth(self.y_points(), t)

    def y_points(self) -> Iterator[int]:
        y = 0
        y_vel = self.y_vel
        while True:
            yield y
            y += y_vel
            y_vel -= 1

    def x_points(self) -> Iterator[int]:
        x = 0
        x_vel = self.x_vel
        while True:
            yield x
            x += x_vel

            if x_vel > 0:
                x_vel -= 1