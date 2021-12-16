from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import cached_property
from typing import Iterator


@dataclass
class Solver(ABC):
    @property
    @abstractmethod
    def solution(self) -> int:
        ...

@dataclass
class Packet(ABC):
    version: int
    sub_packets: list[Packet]

    @property
    @abstractmethod
    def value(self) -> int:
        ...

    def all_packets(self) -> Iterator[Packet]:
        yield self
        for p in self.sub_packets:
            yield from p.all_packets()

@dataclass
class LiteralPacket(Packet):
    bits: str

    @property
    def value(self) -> int:
        return int(self.bits, 2)

class SumPacket(Packet):
    @property
    def value(self) -> int:
        return sum([p.value for p in self.sub_packets])

class ProductPacket(Packet):
    @property
    def value(self) -> int:
        product = 1
        for p in self.sub_packets:
            product *= p.value
        return product

class MinPacket(Packet):
    @property
    def value(self) -> int:
        return min([p.value for p in self.sub_packets])

class MaxPacket(Packet):
    @property
    def value(self) -> int:
        return max([p.value for p in self.sub_packets])

class LessThanPacket(Packet):
    @property
    def value(self) -> int:
        assert len(self.sub_packets) == 2
        a, b = self.sub_packets
        return 1 if a.value < b.value else 0

class GreaterThanPacket(Packet):
    @property
    def value(self) -> int:
        assert len(self.sub_packets) == 2
        a, b = self.sub_packets
        return 1 if a.value > b.value else 0

class EqualToPacket(Packet):
    @property
    def value(self) -> int:
        assert len(self.sub_packets) == 2
        a, b = self.sub_packets
        return 1 if a.value == b.value else 0


@dataclass
class PacketReader(object):
    bits: str
    index: int = 0

    def read(self) -> Packet:
        version = int(self.bits[self.index:self.index+3], 2)
        type_id = int(self.bits[self.index+3:self.index+6], 2)

        if type_id == 4:
            self.index += 6
            return self.read_literal(version, type_id)
        else:
            length_type_id = int(self.bits[self.index+6])
            self.index += 7
            if length_type_id == 0:
                return self.read_length_type_0(version, type_id)
            else:
                return self.read_length_type_1(version, type_id)

    def read_literal(self, version: int, type_id: int) -> Packet:
        chunks = list[str]()
        while self.bits[self.index] == "1":
            chunks.append(self.bits[self.index + 1: self.index+5])
            self.index += 5
        chunks.append(self.bits[self.index + 1: self.index+5])
        self.index += 5
        bits = "".join(chunks)
        return LiteralPacket(version=version, bits=bits, sub_packets=[])

    def read_length_type_0(self, version: int, type_id: int) -> Packet:
        total_subpacket_length = int(self.bits[self.index:self.index + 15], 2)
        self.index += 15
        end_index = self.index + total_subpacket_length
        sub_packets = list[Packet]()
        while self.index < end_index:
            sub_packets.append(self.read())
        return self.create_operator_packet(version=version, type_id=type_id, sub_packets=sub_packets)

    def read_length_type_1(self, version: int, type_id: int) -> Packet:
        number_of_subpackets = int(self.bits[self.index:self.index+11], 2)
        self.index += 11
        sub_packets = [self.read() for _ in range(number_of_subpackets)]
        return self.create_operator_packet(version=version, type_id=type_id, sub_packets=sub_packets)

    def create_operator_packet(self, version: int, type_id: int, sub_packets: list[Packet]) -> Packet:
        match type_id:
            case 0:
                return SumPacket(version=version, sub_packets=sub_packets)
            case 1:
                return ProductPacket(version=version, sub_packets=sub_packets)
            case 2:
                return MinPacket(version=version, sub_packets=sub_packets)
            case 3:
                return MaxPacket(version=version, sub_packets=sub_packets)
            case 5:
                return GreaterThanPacket(version=version, sub_packets=sub_packets)
            case 6:
                return LessThanPacket(version=version, sub_packets=sub_packets)
            case 7:
                return EqualToPacket(version=version, sub_packets=sub_packets)
            case _:
                raise Exception(f"type_id {type_id} isn't for operators, ya goof!")

    # @cached_property
    # def packets(self) -> list[PacketReader]:
    #     if self.is_literal:
    #         return [self]

    # @cached_property
    # def version(self) -> int:
    #     return int(self.bits[self.global_index(0):self.global_index(3)], 2)

    # @cached_property
    # def type_id(self) -> int:
    #     return int(self.bits[self.global_index(3):self.global_index(6)], 2)

    # @cached_property
    # def length_type_id(self) -> int:
    #     assert not self.is_literal
    #     return int(self.bits[self.global_index(6)])
    
    # def literal_bits(self) -> str:
    #     chunks = list[str]()
    #     index = self.global_index(6)
    #     while self.bits[index] == "1":
    #         chunks.append(self.bits[index + 1: index+5])
    #         index += 5
    #     chunks.append(self.bits[index + 1: index+5])
    #     return "".join(chunks)

    # def length_type_0_bits(self) -> str:
    #     assert self.length_type_id == 0
    #     total_subpacket_length = int(self.bits[self.global_index(7):self.global_index(7+15)], 2)

    def length_type_1_bits(self) -> str:
        assert self.length_type_id == 1
        number_of_subpackets = int(self.bits[self.global_index(7):self.global_index(7+11)], 2)

    def global_index(self, relative_index: int):
        return self.start + relative_index
