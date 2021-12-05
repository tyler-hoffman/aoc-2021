from src.day_05.shared import Parser, Solver


def solve(input: str) -> int:
    parser = Parser()
    lines = [line for line in parser.parse(input)]
    return Solver(lines).solution


if __name__ == "__main__":
    with open("src/day_05/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
