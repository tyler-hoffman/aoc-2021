from dataclasses import dataclass

from src.day_16.models import (
    EqualToPacket,
    GreaterThanPacket,
    LessThanPacket,
    LiteralPacket,
    MaxPacket,
    MinPacket,
    Packet,
    ProductPacket,
    SumPacket,
)


@dataclass
class PacketReader(object):
    bits: str
    index: int = 0

    def read(self) -> Packet:
        version = int(self.bits[self.index : self.index + 3], 2)
        type_id = int(self.bits[self.index + 3 : self.index + 6], 2)

        if type_id == 4:
            self.index += 6
            return self.read_literal(version, type_id)
        else:
            length_type_id = int(self.bits[self.index + 6])
            self.index += 7
            if length_type_id == 0:
                return self.read_length_type_0(version, type_id)
            else:
                return self.read_length_type_1(version, type_id)

    def read_literal(self, version: int, type_id: int) -> Packet:
        chunks = list[str]()
        while self.bits[self.index] == "1":
            chunks.append(self.bits[self.index + 1 : self.index + 5])
            self.index += 5
        chunks.append(self.bits[self.index + 1 : self.index + 5])
        self.index += 5
        bits = "".join(chunks)
        return LiteralPacket(version=version, bits=bits, sub_packets=[])

    def read_length_type_0(self, version: int, type_id: int) -> Packet:
        total_subpacket_length = int(self.bits[self.index : self.index + 15], 2)
        self.index += 15
        end_index = self.index + total_subpacket_length
        sub_packets = list[Packet]()
        while self.index < end_index:
            sub_packets.append(self.read())
        return self.create_operator_packet(
            version=version, type_id=type_id, sub_packets=sub_packets
        )

    def read_length_type_1(self, version: int, type_id: int) -> Packet:
        number_of_subpackets = int(self.bits[self.index : self.index + 11], 2)
        self.index += 11
        sub_packets = [self.read() for _ in range(number_of_subpackets)]
        return self.create_operator_packet(
            version=version, type_id=type_id, sub_packets=sub_packets
        )

    def create_operator_packet(
        self, version: int, type_id: int, sub_packets: list[Packet]
    ) -> Packet:
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
