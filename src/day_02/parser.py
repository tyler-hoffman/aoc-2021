from typing import List
from .models import Direction, Down, Forward, Up


class Parser(object):
    @staticmethod
    def parse(input: str) -> List[Direction]:
        return [Parser.parse_line(line) for line in input.splitlines() if line]

    @staticmethod
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
