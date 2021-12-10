from functools import reduce


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Adjacent:
    def __init__(self, x: int, y: int, height: int) -> None:
        self.point = Point(x, y)
        self.height = height


def parseFile(input: 'list[str]') -> 'list[list[int]]':
    heightmap: 'list[list[int]]' = []
    for line in input:
        row: 'list[int]' = []
        for cell in line:
            row.append(int(cell))
        heightmap.append(row)
    return heightmap


def findAdjacents(heightmap: 'list[list[int]]') -> 'list[int]':
    adjacents: 'list[Adjacent]' = []
    for y, row in enumerate(heightmap):
        for x, cell in enumerate(row):
            # Corners
            if x == 0 and y == 0:
                if cell < heightmap[y][x+1] and cell < heightmap[y+1][x]:
                    adjacents.append(Adjacent(x, y, cell))
            elif x == 0 and y == len(heightmap) - 1:
                if cell < heightmap[y-1][x] and cell < heightmap[y][x+1]:
                    adjacents.append(Adjacent(x, y, cell))
            elif x == len(row) - 1 and y == 0:
                if cell < heightmap[y][x-1] and cell < heightmap[y+1][x]:
                    adjacents.append(Adjacent(x, y, cell))
            elif x == len(row) - 1 and y == len(heightmap) - 1:
                if cell < heightmap[y][x-1] and cell < heightmap[y-1][x]:
                    adjacents.append(Adjacent(x, y, cell))
            # Edges
            elif x == 0 and y < len(heightmap) - 1:
                if cell < heightmap[y-1][x] and cell < heightmap[y][x+1] and cell < heightmap[y+1][x]:
                    adjacents.append(Adjacent(x, y, cell))
            elif x == len(row) - 1 and y < len(heightmap) - 1:
                if cell < heightmap[y][x-1] and cell < heightmap[y-1][x] and cell < heightmap[y+1][x]:
                    adjacents.append(Adjacent(x, y, cell))
            elif y == 0 and x < len(row) - 1:
                if cell < heightmap[y][x-1] and cell < heightmap[y][x+1] and cell < heightmap[y+1][x]:
                    adjacents.append(Adjacent(x, y, cell))
            elif y == len(heightmap) - 1 and x < len(row) - 1:
                if cell < heightmap[y][x-1] and cell < heightmap[y-1][x] and cell < heightmap[y][x+1]:
                    adjacents.append(Adjacent(x, y, cell))
            # Rest
            else:
                if cell < heightmap[y][x-1] and cell < heightmap[y-1][x] and cell < heightmap[y][x+1] and cell < heightmap[y+1][x]:
                    adjacents.append(Adjacent(x, y, cell))
    return adjacents


def sumLowPoints(adjacents: 'list[Adjacent]') -> int:
    sum = 0
    for item in adjacents:
        sum += item.height + 1
    return sum


def getBassinSizes(heightmap: 'list[list[int]]', adjacents: 'list[Adjacent]') -> 'list[int]':

    def getBassinSize(heightmap, adjacent: Adjacent):
        maxWidth, maxHeight = (len(heightmap[0]), len(heightmap))
        array = [d[:] for d in heightmap]

        def filler(x, y):
            if x < 0 or y < 0 or x >= maxWidth or y >= maxHeight:
                # Bounds check.
                return

            if array[y][x] >= 9:
                # Boundary check.
                return

            array[y][x] = 10    # use this to distinguish filled points.

            filler(x, y - 1)    # North
            filler(x, y + 1)    # South
            filler(x + 1, y)    # East
            filler(x - 1, y)    # West

        filler(adjacent.point.x, adjacent.point.y)

        return sum([row.count(10) for row in array])

    bassinSizes: 'list[int]' = []
    for adjacent in adjacents:
        bassinSizes.append(getBassinSize(heightmap, adjacent))

    top3Basins = sorted(bassinSizes)[-3:]
    product = 1
    for bassin in top3Basins:
        product *= bassin
    return product


with open("9/input.txt", "r") as file:
    heightmap = parseFile(input=file.read().splitlines())
adjacents = findAdjacents(heightmap)
print(f"accumulated risk: {sumLowPoints(adjacents)}")
print(f"product of bassin sizes: {getBassinSizes(heightmap,adjacents)}")
