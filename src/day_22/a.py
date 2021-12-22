from dataclasses import dataclass
from functools import cached_property
from src.day_22.models import Cuboid, Instruction, Point3D
from src.day_22.parser import Parser
from src.day_22.solver import Solver


@dataclass
class Day22PartASolver(Solver):
    instructions: list[Instruction]

    @property
    def solution(self) -> int:
        return len(self.all_on_points)

    @cached_property
    def all_on_points(self) -> set[Point3D]:
        output = set[Point3D]()

        for instruction in self.bounded_instructions:
            for point in instruction.cuboid.all_contained_points():
                if instruction.on:
                    output.add(point)
                elif point in output:
                    output.remove(point)

        return output

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
