from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property

from src.day_17.models import TargetArea


@dataclass
class Solver(ABC):
    target_area: TargetArea

    @cached_property
    def min_x_vel_to_check(self) -> int:
        x_vel = 0
        max_x = 0

        while max_x < self.target_area.x_min:
            x_vel += 1
            max_x += x_vel
        return x_vel

    @cached_property
    def max_x_vel_to_check(self) -> int:
        return self.target_area.x_max + 1

    @cached_property
    def min_y_vel_to_check(self) -> int:
        return self.target_area.y_min - 1

    @cached_property
    def max_y_vel_to_check(self) -> int:
        return -1 - self.target_area.y_min
