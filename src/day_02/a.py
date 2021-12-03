from typing import List
from src.day_02.shared import Direction, Down, Up, parse
from src.utils.point import Point


def follow_directions(directions: List[Direction]) -> Point:
    point = Point(x=0, y=0)

    for direction in directions:
        match direction:
            case Up(value=value):
                point += Point(x=0, y=-direction.value)
            case Down(value=value):
                point += Point(x=0, y=direction.value)
            case _:
                point += Point(x=direction.value, y=0)
    return point


def solve(input: str) -> int:
    directions = parse(input)

    point = follow_directions(directions)

    return point.x * point.y

if __name__ == "__main__":
    with open("src/day_02/input.txt", "r") as f:
        input = f.read()
    print(input)