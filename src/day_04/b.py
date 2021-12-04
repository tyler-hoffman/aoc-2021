from typing import Set
from src.day_04.shared import parse


def solve(input: str) -> int:
    data = parse(input)
    remaining_boards = data.boards.copy()

    to_check: Set[int] = set()
    for item in data.picks:
        to_check.add(item)

        for board in remaining_boards:
            if board.has_match(to_check):
                if len(remaining_boards) > 1:
                    remaining_boards.remove(board)
                else:
                    unmarked = board.unmarked_stuff(to_check)
                    return sum(unmarked) * item


if __name__ == "__main__":
    with open("src/day_04/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
