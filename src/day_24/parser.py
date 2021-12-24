from __future__ import annotations
from dataclasses import dataclass

from src.day_24.models import BinaryOperator, BinaryOperatorType, InputOperator, Operator


@dataclass
class Parser(object):
    input: str
    operator_count: int = -1

    def parse(self) -> list[Operator]:
        self.operator_count = -1 
        lines = self.input.strip().splitlines()
        return [self.parse_line(line) for line in lines]

    def parse_line(self, line: str) -> Operator:
        match line.split():
            case ("inp", sets):
                self.operator_count += 1
                return InputOperator(sets=sets, index=self.operator_count)
            case (operator, sets, second):
                return BinaryOperator(binary_operator_type=BinaryOperatorType[operator.upper()], sets=sets, second=second)

