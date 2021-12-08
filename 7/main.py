def parseFile(input: str) -> 'dict[int, int]':
    crabs: list[int] = []
    for crab in input.split(","):
        crabs.append(int(crab))
    crabs.sort()
    return crabs


def calculateAlignment(crabs: 'list[int]', type: int) -> int:
    minValue = getFuelUsage(crabs, 0, type)
    minAlignment = 0
    for alignment in range(crabs[len(crabs)-1]):
        newValue = getFuelUsage(crabs, alignment, type)
        if newValue < minValue:
            minValue = newValue
            minAlignment = alignment
    return minAlignment, minValue


def getFuelUsage(crabs: 'list[int]', alignment: int, type: int) -> int:
    fuel: int = 0
    for crab in crabs:
        if type == 1:  # Part 1
            fuel += abs(crab - alignment)
        elif type == 2:  # Part 2
            tmp = abs(crab - alignment)
            while tmp > 0:
                fuel += tmp
                tmp -= 1
    return fuel


with open("7/input.txt", "r") as file:
    crabs = parseFile(input=file.read().splitlines()[0])
alignment1, fuel1 = alignment = calculateAlignment(crabs, 1)
print(f"fuel usage Part 1: {fuel1}")
alignment2, fuel2 = alignment = calculateAlignment(crabs, 2)
print(f"fuel usage Part 2: {fuel2}")
