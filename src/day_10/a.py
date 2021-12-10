from dataclasses import dataclass
from functools import cached_property
from typing import Optional
from src.day_10.parser import Parser
from src.day_10.solver import Solver


@dataclass
class Corruption(object):
    index: int
    char: str

@dataclass
class LineSolver(object):
    line: str

    @cached_property
    def first_corruption(self) -> Optional[Corruption]:
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
        return None


class Day10PartASolver(Solver):
    @property
    def solution(self) -> int:
        corruptions = [LineSolver(line).first_corruption for line in self.lines]
        return sum([self.score_for_error(corruption.char) for corruption in corruptions if corruption])

    @staticmethod
    def score_for_error(char: str) -> int:
        match char:
            case ")":
                return 3
            case "]":
                return 57
            case "}":
                return 1197
            case ">":
                return 25137
            case _:
                raise Exception(f"Unexpected char: {char}")


def solve(input: str) -> int:
    parser = Parser()
    solver = Day10PartASolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_10/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
