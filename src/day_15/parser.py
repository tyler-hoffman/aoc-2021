from src.utils.point import Point


class Parser(object):
    @classmethod
    def parse(cls, input: str) -> dict[Point, int]:
        output = dict[Point, int]()
        lines = input.strip().splitlines()
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                output[Point(x=x, y=y)] = int(char)
        return output
