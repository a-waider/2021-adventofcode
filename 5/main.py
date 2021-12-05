

from typing import overload


class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Coordinate, p2: Coordinate) -> None:
        self.p1 = p1
        self.p2 = p2

    def getGradient(self) -> int:
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

    def isDiagonal(self) -> bool:
        return abs(self.p1.x - self.p2.x) == abs(self.p1.y-self.p2.y)

    def isHorizontal(self) -> bool:
        return self.p1.x == self.p2.x

    def isVertical(self) -> bool:
        return self.p1.y == self.p2.y


class CoordinateSystem:
    def __init__(self, size: int):
        self.system = [[]]*size
        for i in range(len(self.system)):
            self.system[i] = [0]*size

    def between(self, i: int, a: int, b: int) -> bool:
        if a < b:
            return a <= i and b >= i
        elif a > b:
            return b <= i and a >= i
        elif a == b:
            return b == i and a == i

    def addLine(self, line: Line, diagonal: bool) -> None:
        if diagonal:
            if line.isDiagonal():
                if line.getGradient() == 1:
                    if line.p1.x < line.p2.x and line.p1.y < line.p2.y:
                        anchor = line.p1
                    else:
                        anchor = line.p2
                    for i in range(abs(line.p1.x - line.p2.x)+1):
                        self.system[anchor.x + i][anchor.y + i] += 1
                elif line.getGradient() == -1:
                    if line.p1.x < line.p2.x and line.p2.y < line.p1.y:
                        anchor = line.p1
                    else:
                        anchor = line.p2
                    for i in range(abs(line.p1.x - line.p2.x)+1):
                        self.system[anchor.x + i][anchor.y - i] += 1
        if line.isHorizontal():
            for j in range(len(self.system)):
                if self.between(j, line.p1.y, line.p2.y):
                    self.system[line.p1.x][j] += 1
        elif line.isVertical():
            for j in range(len(self.system)):
                if self.between(j, line.p1.x, line.p2.x):
                    self.system[j][line.p1.y] += 1

    def printSystem(self) -> None:
        for row in self.system:
            for cell in row:
                if cell == 0:
                    print(".", end="")
                else:
                    print(cell, end="")
            print()

    def overlapping(self, threshold: int) -> int:
        overlapping = 0
        for row in self.system:
            for cell in row:
                if cell >= threshold:
                    overlapping += 1
        return overlapping


def parseFile(input: str, diagonal: bool) -> CoordinateSystem:
    maxValue = 999
    system = CoordinateSystem(maxValue)
    for line in input:
        p1Str = line.split(" -> ")[0]
        p2Str = line.split(" -> ")[1]
        p1 = Coordinate(int(p1Str.split(",")[0]), int(p1Str.split(",")[1]))
        p2 = Coordinate(int(p2Str.split(",")[0]), int(p2Str.split(",")[1]))
        system.addLine(Line(p1, p2), diagonal)
    return system


with open("5/input.txt", "r") as file:
    input = file.read().splitlines()
    system1 = parseFile(input, False)
    system2 = parseFile(input, True)
print(f"overlapping (horizontal, vertical): {system1.overlapping(2)}")
print(
    f"overlapping (horizontal, vertical, diagonal): {system2.overlapping(2)}")
