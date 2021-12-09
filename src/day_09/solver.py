from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.day_09.models import Grid


@dataclass
class Solver(ABC):
    grid: Grid

    @property
    @abstractmethod
    def solution(self) -> int:
        ...
