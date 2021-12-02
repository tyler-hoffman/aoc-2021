from typing import List
from src.day_02.shared import Direction, Down, Forward, Up, follow_directions, parse
from src.utils.point import Point


def follow_directions(directions: List[Direction]) -> Point:
    point = Point(x=0, y=0)

    for direction in directions:
        if isinstance(direction, Up):
            point = point.add(Point(x=0, y=-direction.x))
        elif isinstance(direction, Down):
            point = point.add(Point(x=0, y=direction.x))
        else:
            point = point.add(Point(x=direction.x, y=0))
    return point


def solve(input: str) -> int:
    directions = parse(input)

    point = follow_directions(directions)

    return point.x * point.y


if __name__ == "__main__":
    with open("src/day_02/input.txt", "r") as f:
        input = f.read()
    output = solve(input)
    print(output)
