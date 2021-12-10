from src.day_10.parser import Parser
from src.day_10.solver import Incomplete, LineSolver, Solver

class Day10PartBSolver(Solver):
    @property
    def solution(self) -> int:
        results = [LineSolver(line).result for line in self.lines]
        incompletes = [result for result in results if isinstance(result, Incomplete)]
        scores = [self.score_incomplete(incomplete.missing) for incomplete in incompletes]

        return self.middle_value(scores)

    def score_incomplete(self, chars: list[str]) -> int:
        output = 0

        for char in chars:
            output *= 5
            output += self.score_for_char(char)

        return output

    def middle_value(self, values: list[int]) -> int:
        length = len(values)
        assert length % 2 == 1

        return sorted(values)[length // 2]

    @staticmethod
    def score_for_char(char: str) -> int:
        match char:
            case ")":
                return 1
            case "]":
                return 2
            case "}":
                return 3
            case ">":
                return 4
            case _:
                raise Exception(f"Unexpected char: {char}")



def solve(input: str) -> int:
    parser = Parser()
    solver = Day10PartBSolver(parser.parse(input))

    return solver.solution


if __name__ == "__main__":
    with open("src/day_10/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
