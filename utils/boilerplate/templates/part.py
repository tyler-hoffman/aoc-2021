PART_TEMPLATE = """
def solve(input: str) -> int:
    return -1


def solve_for_file() -> int:
    with open("src/day_{day_string}/input.txt", "r") as f:
        input = f.read()
    return solve(input)

if __name__ == "__main__":
    print(solve_for_file())

"""
