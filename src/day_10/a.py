from src.day_10.parser import Parser
from src.day_10.solver import Corruption, LineSolver, Solver


class Day10PartASolver(Solver):
    @property
    def solution(self) -> int:
        results = [LineSolver(line).result for line in self.lines]
        return sum([self.score_for_char(result.char) for result in results if isinstance(result, Corruption)])

    @staticmethod
    def score_for_char(char: str) -> int:
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
