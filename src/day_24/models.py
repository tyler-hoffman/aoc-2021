from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class State(object):
    w: int = 0
    x: int = 0
    y: int = 0
    z: int = 0

    def get(self, var: str) -> int:
        match var:
            case "w":
                return self.w
            case "x":
                return self.x
            case "y":
                return self.y
            case "z":
                return self.z

    def set(self, var: str, val: int) -> State:
        w = self.w
        x = self.x
        y = self.y
        z = self.z
        match var:
            case "w":
                w = val
            case "x":
                x = val
            case "y":
                y = val
            case "z":
                z = val
        return State(w, x, y, z)


class BinaryOperatorType(Enum):
    ADD = 1
    MUL = 2
    DIV = 3
    MOD = 4
    EQL = 5

@dataclass(frozen=True)
class Operator(ABC):
    sets: str

    @property
    @abstractmethod
    def depends(self) -> set[str]:
        ...


@dataclass(frozen=True)
class InputOperator(Operator):
    index: int

    @property
    def depends(self) -> set[str]:
        return set()

@dataclass(frozen=True)
class BinaryOperator(Operator):
    second: int | str
    binary_operator_type: BinaryOperatorType

    @property
    def depends(self) -> set[str]:
        match self.second:
            case int() as second:
                return {self.sets, second}
            case _:
                return {self.sets}
