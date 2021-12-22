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
        bounded_instructions = [
            Instruction(cuboid=self.cuboid_to_bounds(i.cuboid), on=i.on)
            for i in self.instructions
            if self.in_range(i.cuboid)
        ]
        return [
            instruction
            for instruction in bounded_instructions
            if instruction.cuboid.is_valid
        ]

    def cuboid_to_bounds(self, cuboid: Cuboid) -> Cuboid:
        return Cuboid(
            min=Point3D(
                x=self.to_range(cuboid.min.x),
                y=self.to_range(cuboid.min.y),
                z=self.to_range(cuboid.min.z),
            ),
            max=Point3D(
                x=self.to_range(cuboid.max.x),
                y=self.to_range(cuboid.max.y),
                z=self.to_range(cuboid.max.z),
            ),
        )

    def in_range(self, cuboid: Cuboid) -> bool:
        return all(
            [
                cuboid.min.x <= 50,
                cuboid.min.z <= 50,
                cuboid.min.z <= 50,
                cuboid.max.x >= -50,
                cuboid.max.y >= -50,
                cuboid.max.z >= -50,
            ]
        )

    def to_range(self, value: int) -> int:
        if value > 50:
            return 50
        elif value < -50:
            return -50
        else:
            return value


def solve(input: str) -> int:
    instructions = Parser.parse(input)
    solver = Day22PartASolver(instructions=instructions)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_22/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
