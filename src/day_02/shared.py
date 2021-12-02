import dataclasses
from src.utils.point import Point
from typing import List


@dataclasses.dataclass
class Direction(object):
    value: int


class Up(Direction):
    pass


class Down(Direction):
    pass


class Forward(Direction):
    pass


def parse_line(line: str) -> Direction:
    direction, magnitude_string = line.split(" ")
    magnitude = int(magnitude_string)

    if direction == "up":
        return Up(value=magnitude)
    elif direction == "down":
        return Down(value=magnitude)
    elif direction == "forward":
        return Forward(value=magnitude)
    else:
        raise Exception(f"Unexpected direction: {direction}")


def parse(input: str) -> List[Direction]:
    return [parse_line(line) for line in input.splitlines() if line]
