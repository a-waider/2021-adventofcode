from typing import Tuple


class InvalidOrientation(Exception):
    pass


class FoldInstruction:
    def __init__(self, orientation: str, value: int):
        if orientation == "x" or orientation == "y":
            self.orientation = orientation
            self.value = value
        else:
            raise InvalidOrientation("Orientation must be \"x\" or \"y\"")


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Grid:
    def __init__(self, dots: 'list[Point]'):
        maxX = 0
        maxY = 0
        for dot in dots:
            if dot.x > maxX:
                maxX = dot.x
            if dot.y > maxY:
                maxY = dot.y
        self.grid: list[list[bool]] = []
        for i in range(maxY+1):
            self.grid.append([False]*(maxX+1))
        for dot in dots:
            self.grid[dot.y][dot.x] = True

    def fold(self, foldInstructions: 'list[FoldInstruction]') -> None:
        for foldInstruction in foldInstructions:
            if foldInstruction.orientation == "x":
                columnsToRemove = set()
                for y, row in enumerate(self.grid):
                    for x, cell in enumerate(row):
                        if x >= foldInstruction.value:
                            if self.grid[y][x]:
                                self.grid[y][x-2 *
                                             (x-foldInstruction.value)] = True
                            columnsToRemove.add(x)
                for row in self.grid:
                    for column in reversed(sorted(columnsToRemove)):
                        row.pop(column)
            elif foldInstruction.orientation == "y":
                rowsToRemove = []
                for y, row in enumerate(self.grid):
                    if y >= foldInstruction.value:
                        for x, cell in enumerate(row):
                            if self.grid[y][x]:
                                self.grid[y-2 *
                                          (y-foldInstruction.value)][x] = True
                        rowsToRemove.append(y)
                for row in reversed(rowsToRemove):
                    self.grid.pop(row)

    def countDots(self) -> int:
        dots = 0
        for row in self.grid:
            for cell in row:
                if cell:
                    dots += 1
        return dots

    def __str__(self) -> str:
        string = ""
        for row in self.grid:
            for cell in row:
                if cell:
                    string += "#"
                else:
                    string += "."
            string += "\n"
        return string[:-1]


def parseFile(lines: 'list[str]'):  # -> Tuple(Grid, 'list[FoldInstruction]'):
    # lines = [
    #     "6,10",
    #     "0,14",
    #     "9,10",
    #     "0,3",
    #     "10,4",
    #     "4,11",
    #     "6,0",
    #     "6,12",
    #     "4,1",
    #     "0,13",
    #     "10,12",
    #     "3,4",
    #     "3,0",
    #     "8,4",
    #     "1,10",
    #     "2,14",
    #     "8,10",
    #     "9,0",
    #     "",
    #     "fold along y=7",
    #     "fold along x=5",
    # ]
    dots: list[Point] = []
    foldInstructions: list[FoldInstruction] = []
    for line in lines:
        if "," in line:  # Dot
            dots.append(
                Point(int(line.split(",")[0]), int(line.split(",")[1])))
        elif "fold along" in line:  # Fold instruction
            cleared = line.replace("fold along ", "")
            foldInstructions.append(FoldInstruction(
                cleared.split("=")[0], int(cleared.split("=")[1])))
    grid = Grid(dots)
    return grid, foldInstructions


with open("13/input.txt", "r") as file:
    grid, foldInstructions = parseFile(lines=file.read().splitlines())
grid.fold([foldInstructions[0]])
print(f"dots after first fold: {grid.countDots()}")
grid.fold(foldInstructions[1:])
print("Code:")
print(grid)
