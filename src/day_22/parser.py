import re
from src.day_22.models import Cuboid, Instruction, Point3D


class Parser(object):
    @staticmethod
    def parse(input: str) -> list[Instruction]:
        lines = input.strip().splitlines()
        return [Parser.parse_line(line) for line in lines]

    @staticmethod
    def parse_line(line: str) -> Instruction:
        on_or_off = line.split()[0]
        assert on_or_off in {"on", "off"}

        xa, xb, ya, yb, za, zb = [int(x) for x in re.findall("-?\d+", line)]
        cuboid = Cuboid(
            min=Point3D(
                x=min([xa, xb]),
                y=min([ya, yb]),
                z=min([za, zb]),
            ),
            max=Point3D(
                x=max([xa, xb]),
                y=max([ya, yb]),
                z=max([za, zb]),
            ),
        )
        return Instruction(cuboid=cuboid, on=on_or_off == "on")
