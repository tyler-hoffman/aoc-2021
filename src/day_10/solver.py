from __future__ import annotations
from dataclasses import dataclass, field
from functools import cached_property
from typing import Dict, Type


@dataclass
class BacketInfo(object):
    @cached_property
    def opening_to_closing(self) -> Dict[str, str]:
        return {
            "(": ")",
            "[": "]",
            "{": "}",
            "<": ">",
        }

    @cached_property
    def closing_to_opening(self) -> Dict[str, str]:
        return {v: k for k, v in self.opening_to_closing.items()}

    @cached_property
    def opening(self) -> set[str]:
        return set(self.opening_to_closing.keys())

    @cached_property
    def closing(self) -> set[str]:
        return set(self.opening_to_closing.values())


@dataclass
class Solver():
    lines: list[str]

    @cached_property
    def incompletes(self) -> list[Incomplete]:
        return [result for result in self.results if isinstance(result, Incomplete)]

    @cached_property
    def corruptions(self) -> list[Corruption]:
        return [result for result in self.results if isinstance(result, Corruption)]

    @cached_property
    def results(self) -> Result:
        return [LineSolver(line).result for line in self.lines]


@dataclass
class LineSolver(object):
    line: str
    bracket_info: BacketInfo = field(default_factory=BacketInfo)

    @cached_property
    def result(self) -> Result:
        stack: list[str] = []
        for index, char in enumerate(self.line):
            if char in self.bracket_info.opening:
                stack.append(char)
            elif char in self.bracket_info.closing:
                if len(stack) == 0 or stack[-1] != self.bracket_info.closing_to_opening[char]:
                    return Corruption(index=index, char=char)
                else:
                    stack.pop()
            else:
                raise Exception(f"Unexpected char: {char}")

        if len(stack):
            missing = [self.bracket_info.opening_to_closing[char] for char in stack[::-1]]
            return Incomplete(missing=missing)
        else:
            return Success()


@dataclass
class Corruption(object):
    index: int
    char: str

@dataclass
class Incomplete(object):
    missing: list[str]

class Success(object):
    pass

Result = Corruption | Incomplete | Success
