from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterator


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
