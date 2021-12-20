from dataclasses import dataclass
from src.day_20.models import Image

from src.utils.point import Point


@dataclass
class Data(object):
    algorithm: list[bool]
    image: Image


class Parser(object):
    @staticmethod
    def parse(input: str) -> Data:
        lines = input.strip().splitlines()
        lines = [line.strip() for line in lines]

        algorithm_lines = list[str]()
        input_image_lines = list[str]()
        list_to_append_to = algorithm_lines
        for line in lines:
            if not line:
                list_to_append_to = input_image_lines
            else:
                list_to_append_to.append(line)
        
        algorithm = Parser.parse_algorithm("".join(algorithm_lines))
        input_image = Parser.input_image_lines_to_set(input_image_lines)

        return Data(
            algorithm=algorithm,
            image=Image(
                pixels=input_image,
                min_x=0,
                min_y=0,
                max_x=len(input_image_lines[0]),
                max_y=len(input_image_lines),
            ),
        )
        
    @staticmethod
    def parse_algorithm(line: str) -> list[bool]:
        return [ch == '#' for ch in line]

    @staticmethod
    def input_image_lines_to_set(lines: list[str]) -> set[Point]:
        output = set[Point]()
        for y, line in enumerate(lines):
            for x, ch in enumerate(line):
                if ch == "#":
                    output.add(Point(x=x, y=y))
        return output
