from typing import Dict
from src.day_05.shared import Parser, get_points_in_line
from src.utils.point import Point


def solve(input: str) -> int:
    parser = Parser()
    lines = [line for line in parser.parse(input)]
    visits: Dict[Point, int] = {}
    for line in lines:
        for point in get_points_in_line(line):
            visits[point] = visits.get(point, 0) + 1

    return len([v for v in visits.values() if v > 1])


if __name__ == "__main__":
    with open("src/day_05/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
