from src.day_01.parser import Parser
from src.day_01.solver import Solver
from src.utils.iterators import sliding_window


class Day01BSolver(Solver):
    @property
    def solution(self) -> int:
        triples = sliding_window(self.numbers, 3)
        sums = [sum(t) for t in triples]
        adjacent_sums = sliding_window(sums, 2)

        return self.count_ascending(adjacent_sums)


def solve(input: str) -> int:
    parser = Parser()
    solver = Day01BSolver(numbers=parser.parse(input))
    return solver.solution


if __name__ == "__main__":
    with open("src/day_01/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
