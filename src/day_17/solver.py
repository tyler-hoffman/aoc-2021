from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property

from src.day_17.models import TargetArea


@dataclass
class Solver(ABC):
    target_area: TargetArea

    @cached_property
    def max_y_vel(self) -> int:
        return -1 - self.target_area.y_min
