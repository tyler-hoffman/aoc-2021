from typing import List, Tuple, TypeVar
from src.day_01.shared import parse


T = TypeVar("T")

def get_adjacent_items(items: List[T]) -> List[Tuple[T, T]]:
    return list(zip(items[:-1], items[1:]))

def solve(input: str) -> int:
    numbers = parse(input)

    adjacent_items = get_adjacent_items(numbers)

    return len([a for a, b in adjacent_items if b > a])


if __name__ == "__main__":
    input = open("src/day_01/input.txt", "r").read()
    output = solve(input)
    print(output)
