from parameterized import parameterized
import unittest
from src.day_16.parser import Parser

from src.day_16.solver import PacketReader

from src.day_16.a import solve


class TestDay16A(unittest.TestCase):
    def test_evaluates_literal(self):
        bits = Parser.parse("D2FE28")
        packet_reader = PacketReader(bits)

        self.assertEqual(packet_reader.read().value, 2021)

    def test_length_type_0(self):
        bits = Parser.parse("38006F45291200")
        packet_reader = PacketReader(bits)
        packet = packet_reader.read()

        self.assertEqual(len(packet.sub_packets), 2)

    def test_length_type_1(self):
        bits = Parser.parse("EE00D40C823060")
        packet_reader = PacketReader(bits)
        packet = packet_reader.read()

        self.assertEqual(len(packet.sub_packets), 3)

    @parameterized.expand(
        [
            ("8A004A801A8002F478", 16),
            ("620080001611562C8802118E34", 12),
            ("C0015000016115A2E0802F182340", 23),
            ("A0016C880162017C3686B18A3D4780", 31),
        ]
    )
    def test_solve(self, hex_string: str, expected: int):
        self.assertEqual(solve(hex_string), expected)

    def test_solution(self):
        with open("src/day_16/input.txt", "r") as f:
            input = f.read()
            self.assertEqual(solve(input), 877)
