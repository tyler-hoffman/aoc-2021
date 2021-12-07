from src.day_01.parser import Parser
from src.day_01.solver import Solver
from src.utils.iterators import sliding_window


class Day01ASolver(Solver):
    @property
    def solution(self) -> int:
        adjacent_items = sliding_window(self.numbers, 2)

        return self.count_ascending(adjacent_items)


def solve(input: str) -> int:
    parser = Parser()
    solver = Day01ASolver(numbers=parser.parse(input))
    return solver.solution


if __name__ == "__main__":
    with open("src/day_01/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
