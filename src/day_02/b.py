from typing import List
from src.day_02.shared import Direction, Down, Up, parse
from src.utils.point import Point


def follow_directions(directions: List[Direction]) -> Point:
    point = Point(x=0, y=0)
    aim = 0

    for direction in directions:
        match direction:
            case Up(value=value):
                aim -= direction.value
            case Down(value=value):
                aim += direction.value
            case _:
                point += Point(x=direction.value, y=direction.value * aim)
    return point


def solve(input: str) -> int:
    directions = parse(input)

    point = follow_directions(directions)

    return point.x * point.y

def solve_for_file() -> int:
    with open("src/day_02/input.txt", "r") as f:
        input = f.read()
    return solve(input)

if __name__ == "__main__":
    print(solve_for_file())
