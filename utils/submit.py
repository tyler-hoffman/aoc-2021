import aocd
import argparse
import subprocess

from utils.boilerplate.file_data import FileData


def submit(day: int, part: str) -> None:
    data_file = FileData(day=day, part=part)
    completed_process = subprocess.run(["python", "-m", data_file.part_module], capture_output=True)
    answer = completed_process.stdout.decode("utf-8").strip()

    aocd.submit(day=2, part="a", year=2020, answer=answer)

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Helper to submit problems"
    )
    parser.add_argument("-d", "--day", type=int, help="Day to create files for")
    parser.add_argument(
        "-p",
        "--part",
        choices=["a", "b"],
        help="Part to create files for",
    )

    return parser

if __name__ == "__main__":
    args = create_parser().parse_args()

    submit(day=args.day, part=args.part)




