from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property
from typing import List, Tuple

from src.utils.collections import frequency_map


@dataclass
class LineAnalyzer(object):
    lines: List[str]

    @property
    def line_length(self) -> int:
        return len(self.lines[0])

    @property
    def line_count(self) -> int:
        return len(self.lines)

    def zeros_and_ones_for_position(self, index: int) -> Tuple[int, int]:
        freqs = frequency_map([line[index] for line in self.lines])
        zero_count = freqs.get("0", 0)
        one_count = freqs.get("1", 0)

        return zero_count, one_count


@dataclass
class Solver(ABC):
    lines: List[str]

    @property
    @abstractmethod
    def solution(self) -> int:
        ...
