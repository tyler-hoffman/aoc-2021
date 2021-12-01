from src.day_01.shared import parse, sliding_window


def solve(input: str) -> int:
    numbers = parse(input)

    adjacent_items = sliding_window(numbers, 2)

    return len([a for a, b in adjacent_items if b > a])


if __name__ == "__main__":
    input = open("src/day_01/input.txt", "r").read()
    output = solve(input)
    print(output)
