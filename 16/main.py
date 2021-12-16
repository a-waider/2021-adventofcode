from typing import Tuple
from queue import Queue
import math


class Packet:
    def __init__(self, version: int, typeId: int, literal: int = None, subPackets: 'list[Packet]' = None):
        self.version = version
        self.typeId = typeId
        self.literal = literal
        self.subPackets = subPackets


def sumVersions(packet: Packet) -> int:
    if not packet.subPackets:
        return packet.version
    else:
        tmp = packet.version
        for subPacket in packet.subPackets:
            tmp += sumVersions(subPacket)
        return tmp


def calcValue(packet: Packet, method=None) -> int:
    if not packet.subPackets:
        return packet.literal
    else:
        subPacketValues = []
        for subPacket in packet.subPackets:
            if subPacket.literal is None:
                subPacketValues.append(calcValue(subPacket))
            else:
                subPacketValues.append(subPacket.literal)
        if packet.typeId == 0:
            return sum(subPacketValues)
        elif packet.typeId == 1:
            return math.prod(subPacketValues)
        elif packet.typeId == 2:
            return min(subPacketValues)
        elif packet.typeId == 3:
            return max(subPacketValues)
        elif packet.typeId == 4:
            return packet.literal
        elif packet.typeId == 5:
            if subPacketValues[0] > subPacketValues[1]:
                return 1
            else:
                return 0
        elif packet.typeId == 6:
            if subPacketValues[0] < subPacketValues[1]:
                return 1
            else:
                return 0
        elif packet.typeId == 7:
            if subPacketValues[0] == subPacketValues[1]:
                return 1
            else:
                return 0


def parseFile(input: str) -> 'list[Packet]':
    def parsePackets(queue: Queue):
        version = (((queue.get() << 1) + queue.get()) << 1) + queue.get()
        typeId = (((queue.get() << 1) + queue.get()) << 1) + queue.get()
        if typeId == 4:  # literal
            literal = 0
            while True:
                tmp = ((((((queue.get() << 1) + queue.get()) << 1) +
                         queue.get() << 1) + queue.get()) << 1) + queue.get()
                literal <<= 4
                literal += tmp & 0b1111
                if not tmp >> 4:  # last packet
                    break
            return Packet(version, typeId, literal)
        else:  # operator
            if queue.get():  # next 11 bits represents number of subpackets
                countSubPackets = 0
                for _ in range(11):
                    countSubPackets <<= 1
                    countSubPackets += queue.get()
                subPackets = []
                for _ in range(countSubPackets):
                    subPackets.append(parsePackets(queue))
                return Packet(version, typeId, subPackets=subPackets)
            else:  # next 15 bits is the total length of subpackets
                totalLength = 0
                for _ in range(15):
                    totalLength <<= 1
                    totalLength += queue.get()
                content = Queue()
                for _ in range(totalLength):
                    content.put(queue.get())
                subPackets = []
                while not content.empty():
                    subPackets.append(parsePackets(content))
                return Packet(version, typeId, subPackets=subPackets)

    # convert to bits
    queue = Queue()
    for item in input:
        x = int(item, 16)
        for i in reversed(range(4)):
            queue.put((x & (1 << i)) >> i)

    # convert to packets
    packet = parsePackets(queue)

    return packet


with open("16/input.txt", "r") as file:
    packet = parseFile(file.read().splitlines()[0])
print(f"versions sum: {sumVersions(packet)}")
print(f"calculated value: {calcValue(packet)}")
