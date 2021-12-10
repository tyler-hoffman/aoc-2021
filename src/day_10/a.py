from src.day_10.parser import Parser
from src.day_10.solver import Solver


class Day10PartASolver(Solver):
    @property
    def solution(self) -> int:
        return sum(
            [self.score_for_char(corruption.char) for corruption in self.corruptions]
        )

    @staticmethod
    def score_for_char(char: str) -> int:
        return {
            ")": 3,
            "]": 57,
            "}": 1197,
            ">": 25137,
        }[char]


def solve(input: str) -> int:
    parser = Parser()
    solver = Day10PartASolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_10/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
