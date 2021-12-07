from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterator, List, Tuple


@dataclass
class Solver(ABC):
    numbers: List[int]

    @property
    @abstractmethod
    def solution(self) -> int:
        ...

    def count_ascending(self, items: Iterator[Tuple[int, int]]) -> int:
        return len([a for a, b in items if b > a])
