from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


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
