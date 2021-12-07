from functools import cached_property
from typing import List

from src.day_03.parser import Parser
from src.day_03.solver import LineAnalyzer, Solver


class Day03ASolver(Solver):
    @property
    def solution(self) -> int:
        return self.array_to_int(self.gamma_bits) * self.array_to_int(self.epsilon_bits)

    @cached_property
    def line_analyzer(self) -> LineAnalyzer:
        return LineAnalyzer(self.lines)

    @property
    def gamma_bits(self) -> List[str]:
        output: List[str] = []
        for index in range(self.line_analyzer.line_length):
            zero_count, one_count = self.line_analyzer.zeros_and_ones_for_position(
                index
            )
            if zero_count > one_count:
                output.append("0")
            elif one_count > zero_count:
                output.append("1")
            else:
                raise Exception(f"Unknown winner at index {index}")
        return output

    @cached_property
    def epsilon_bits(self) -> List[str]:
        return ["0" if bit == "1" else "1" for bit in self.gamma_bits]

    @staticmethod
    def array_to_int(bits: List[str]) -> int:
        as_str = "".join(bits)
        return int(as_str, 2)


def solve(input: str) -> int:
    solver = Day03ASolver(lines=Parser.parse(input))
    return solver.solution


if __name__ == "__main__":
    with open("src/day_03/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
