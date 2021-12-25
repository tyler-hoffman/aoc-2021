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

@dataclass(frozen=True)
class Module(object):
    a: int
    b: int
    c: int

    def new_z_for_w(self, z: int, w: int) -> int:
        x = int(w != self.b + z % 26)
        y1 = 25 * x + 1
        y2 = (w + self.c) * x
        return (z // self.a) * y1 + y2

    def ws_to_output_zs(self, z: int) -> dict[int, int]:
        """Computes a mapping of input w -> z without duplicate zs

        if 2 ws produce the same z, we pick the larger w
        """
        outputs_to_high_w = dict[int, int]()
        for w in range(1, 10):
            output_z = self.new_z_for_w(z, w)
            outputs_to_high_w[output_z] = w
        
        return {w: z for z, w in outputs_to_high_w.items()}

