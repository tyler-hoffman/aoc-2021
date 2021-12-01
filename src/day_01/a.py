from src.day_01.shared import parse
from src.utils.iterators import sliding_window


def solve(input: str) -> int:
    numbers = parse(input)

    adjacent_items = sliding_window(numbers, 2)

    return len([a for a, b in adjacent_items if b > a])


if __name__ == "__main__":
    with open("src/day_01/input.txt", "r") as f:
        input = f.read()
    output = solve(input)
    print(output)
