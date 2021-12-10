from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property

OPENING_TO_CLOSING = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

OPENING = OPENING_TO_CLOSING.keys()

@dataclass
class Solver(ABC):
    lines: list[str]

    @property
    @abstractmethod
    def solution(self) -> int:
        ...


@dataclass
class LineSolver(object):
    line: str

    @cached_property
    def result(self) -> Result:
        stack: list[str] = []
        for index, char in enumerate(self.line):
            match char:
                case "(":
                    stack.append(char)
                case "[":
                    stack.append(char)
                case "{":
                    stack.append(char)
                case "<":
                    stack.append(char)
                case ")":
                    if len(stack) == 0 or stack[-1] != "(":
                        return Corruption(index=index, char=char)
                    else:
                        stack.pop()
                case "]":
                    if len(stack) == 0 or stack[-1] != "[":
                        return Corruption(index=index, char=char)
                    else:
                        stack.pop()
                case "}":
                    if len(stack) == 0 or stack[-1] != "{":
                        return Corruption(index=index, char=char)
                    else:
                        stack.pop()
                case ">":
                    if len(stack) == 0 or stack[-1] != "<":
                        return Corruption(index=index, char=char)
                    else:
                        stack.pop()
                case _:
                    raise Exception(f"Unexpected char: {char}")

        if len(stack):
            missing = [OPENING_TO_CLOSING[char] for char in stack[::-1]]
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
