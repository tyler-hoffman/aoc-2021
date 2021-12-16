from dataclasses import dataclass
from src.day_16.parser import Parser
from src.day_16.solver import PacketReader


@dataclass
class Day16PartASolver(object):
    bits: str

    @property
    def solution(self) -> int:
        packet_reader = PacketReader(self.bits)
        packet = packet_reader.read()
        version_sum = 0
        for packet in packet.all_packets():
            version_sum += packet.version
        return version_sum


def solve(input: str) -> int:
    bits = Parser.parse(input)
    solver = Day16PartASolver(bits=bits)

    return solver.solution


if __name__ == "__main__":
    with open("src/day_16/input.txt", "r") as f:
        input = f.read()
        print(solve(input))
