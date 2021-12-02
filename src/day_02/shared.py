import dataclasses
from src.utils.point import Point
from typing import List

class Direction(object):
    x: int

@dataclasses.dataclass
class Up(Direction):
    x: int

@dataclasses.dataclass
class Down(Direction):
    x: int

@dataclasses.dataclass
class Forward(Direction):
    x: int


def parse_line(line: str) -> Direction:
    direction, magnitude_string = line.split(" ")
    magnitude = int(magnitude_string)

    if direction == "up":
        return Up(x=magnitude)
    elif direction == "down":
        return Down(x=magnitude)
    elif direction == "forward":
        return Forward(x=magnitude)
    else:
        raise Exception(f"Unexpected direction: {direction}")


def parse(input: str) -> List[Direction]:
    return [parse_line(line) for line in input.splitlines() if line]
