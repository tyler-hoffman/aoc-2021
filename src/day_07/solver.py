from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class Solver(ABC):
    starting_positions: List[int]

    @property
    @abstractmethod
    def solution(self) -> int:
        ...
