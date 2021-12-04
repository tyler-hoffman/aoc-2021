
from typing import List, Set
from src.day_04.shared import parse


def solve(input: str) -> int:
    data = parse(input)

    to_check: Set[int] = set()
    for item in data.picks:
        to_check.add(item)

        for board in data.boards:
            if board.has_match(to_check):
                unmarked = board.unmarked_stuff(to_check)
                return sum(unmarked) * item


if __name__ == "__main__":
    with open("src/day_04/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
