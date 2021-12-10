from src.day_10.parser import Parser
from src.day_10.solver import Solver

class Day10PartBSolver(Solver):
    @property
    def solution(self) -> int:
        scores = [self.score_incomplete(incomplete.missing) for incomplete in self.incompletes]

        return self.middle_value(scores)

    @classmethod
    def score_incomplete(cls, chars: list[str]) -> int:
        output = 0

        for char in chars:
            output *= 5
            output += cls.score_for_char(char)

        return output

    @staticmethod
    def middle_value(values: list[int]) -> int:
        length = len(values)
        assert length % 2 == 1

        return sorted(values)[length // 2]

    @staticmethod
    def score_for_char(char: str) -> int:
        return {
            ")": 1,
            "]": 2,
            "}": 3,
            ">": 4,
        }[char]


def solve(input: str) -> int:
    parser = Parser()
    solver = Day10PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_10/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
