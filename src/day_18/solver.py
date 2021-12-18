from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import cached_property
from typing import Optional


@dataclass
class Solver(ABC):
    @property
    @abstractmethod
    def solution(self) -> int:
        ...

@dataclass
class SnailfishNumber(ABC):
    parent: Optional[SnailfishNumber]

    @property
    @abstractmethod
    def magnitude(self) -> int:
        ...

    @property
    @abstractmethod
    def leftmost(self) -> SnailfishLeafNode:
        ...

    @property
    @abstractmethod
    def rightmost(self) -> SnailfishLeafNode:
        ...


@dataclass
class SnailfishPair(SnailfishNumber):
    left: SnailfishNumber
    right: SnailfishNumber

    @property
    def leftmost(self) -> SnailfishLeafNode:
        return self.left.leftmost

    @property
    def rightmost(self) -> SnailfishLeafNode:
        return self.right.rightmost

    @property
    def magnitude(self) -> int:
        return 3 * self.left.magnitude + 2 * self.right.magnitude

    def __repr__(self) -> str:
        return f"[{self.left},{self.right}]"


@dataclass
class SnailfishLeafNode(SnailfishNumber):
    value: int

    @property
    def leftmost(self) -> SnailfishLeafNode:
        return self

    @property
    def rightmostmost(self) -> SnailfishLeafNode:
        return self

    @property
    def magnitude(self) -> int:
        return self.value

    def __repr__(self) -> str:
        return f"{self.value}"
