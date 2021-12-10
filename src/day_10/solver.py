from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Solver(ABC):
    lines: list[str]

    @property
    @abstractmethod
    def solution(self) -> int:
        ...
