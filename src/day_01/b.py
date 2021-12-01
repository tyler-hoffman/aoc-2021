from src.day_01.shared import parse
from src.utils.iterators import sliding_window


def solve(input: str) -> int:
    numbers = parse(input)

    triples = sliding_window(numbers, 3)
    triple_sums = [sum(t) for t in triples]
    adjacent_sums = sliding_window(triple_sums, 2)

    return len([a for a, b in adjacent_sums if b > a])


if __name__ == "__main__":
    input = open("src/day_01/input.txt", "r").read()
    output = solve(input)
    print(output)
