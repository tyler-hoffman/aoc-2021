from dataclasses import dataclass
from src.day_16.parser import Parser
from src.day_16.solver import PacketReader


@dataclass
class Day16PartBSolver(object):
    bits: str

    @property
    def solution(self) -> int:
        packet_reader = PacketReader(self.bits)
        packet = packet_reader.read()

        return packet.value


def solve(input: str) -> int:
    bits = Parser.parse(input)
    solver = Day16PartBSolver(bits=bits)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_16/input.txt", "r") as f:
        input = f.read()
    print(solve(input))
