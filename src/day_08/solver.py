from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cache
from typing import List

from src.day_08.models import Entry


class NumberInfo(object):
    @staticmethod
    @cache
    def can_determine_value_by_length(value: int) -> bool:
        return value in set([1, 4, 7, 8])

    @staticmethod
    @cache
    def is_unique_length(length: int) -> bool:
        return length in {NumberInfo.value_length(x) for x in [1, 4, 7, 8]}

    @staticmethod
    @cache
    def value_length(value: int) -> int:
        value_lengths = NumberInfo.value_lengths()
        return value_lengths[value]

    @staticmethod
    @cache
    def value_lengths() -> int:
        return {
            0: 6,
            1: 2,
            2: 5,
            3: 5,
            4: 4,
            5: 5,
            6: 6,
            7: 3,
            8: 7,
            9: 6,
        }


@dataclass
class Solver(ABC):
    entries: List[Entry]

    @property
    @abstractmethod
    def solution(self) -> int:
        ...
