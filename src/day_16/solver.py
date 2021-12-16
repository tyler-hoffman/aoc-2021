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
class Packet(object):
    version: int
    type_id: int
    value: int
    sub_packets: list[Packet] = field(default_factory=list)

    def all_packets(self) -> Iterator[Packet]:
        yield self
        for p in self.sub_packets:
            yield from p.all_packets()


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
        value = int("".join(chunks), 2)
        return Packet(version=version, type_id=type_id, value=value)


    def read_length_type_0(self, version: int, type_id: int) -> Packet:
        total_subpacket_length = int(self.bits[self.index:self.index + 15], 2)
        self.index += 15
        end_index = self.index + total_subpacket_length
        sub_packets = list[Packet]()
        while self.index < end_index:
            sub_packets.append(self.read())
        return Packet(version=version, type_id=type_id, value=-1, sub_packets=sub_packets)

    def read_length_type_1(self, version: int, type_id: int) -> Packet:
        number_of_subpackets = int(self.bits[self.index:self.index+11], 2)
        self.index += 11
        sub_packets = [self.read() for _ in range(number_of_subpackets)]
        return Packet(version=version, type_id=type_id, value=-1, sub_packets=sub_packets)


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
