from src.day_24.models import Module
from src.day_24.parser import Parser
from src.day_24.solver import Solver


class Day24PartBSolver(Solver):
    def sorted_ws_to_zs(self, module: Module, z: int) -> list[dict[int, int]]:
        ws_to_output_zs = module.ws_to_output_zs(z, range(9, 0, -1))
        return sorted(ws_to_output_zs.items())


def solve(input: str) -> int:
    modules = Parser.parse(input)
    solver = Day24PartBSolver(modules)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_24/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
