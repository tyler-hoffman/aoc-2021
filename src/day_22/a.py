from dataclasses import dataclass
from functools import cached_property
from src.day_22.models import Cuboid, Instruction, Point3D
from src.day_22.parser import Parser
from src.day_22.solver import Solver


class Day22PartASolver(Solver):
    @cached_property
    def bounded_instructions(self) -> list[Instruction]:
        bounded_cuboids = [
            self.valid_range.intersection(i.cuboid) for i in self.instructions
        ]
        return [
            Instruction(cuboid=c, on=i.on)
            for i, c in zip(self.instructions, bounded_cuboids)
            if c is not None
        ]

    @cached_property
    def valid_range(self) -> Cuboid:
        return Cuboid(
            min=Point3D(-50, -50, -50),
            max=Point3D(50, 50, 50),
        )


def solve(input: str) -> int:
    instructions = Parser.parse(input)
    solver = Day22PartASolver(instructions=instructions)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_22/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
