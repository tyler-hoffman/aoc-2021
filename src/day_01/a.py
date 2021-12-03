from src.day_01.shared import count_ascending, parse
from src.utils.iterators import sliding_window


def solve(input: str) -> int:
    numbers = parse(input)

    adjacent_items = sliding_window(numbers, 2)

    return count_ascending(adjacent_items)


if __name__ == "__main__":
    with open("src/day_01/input.txt", "r") as f:
        input = f.read()
    print(input)
