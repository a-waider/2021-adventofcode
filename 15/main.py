from typing import Tuple
import queue


def lowestRiskPath(riskLevelMap: 'dict[Tuple[int, int], int]') -> int:
    maxX = max(x for x, _ in riskLevelMap.keys())
    maxY = max(y for _, y in riskLevelMap.keys())

    q = queue.PriorityQueue()
    q.put((0, (0, 0)))

    dists = {(0, 0): 0}

    while not q.empty():
        risk, (x, y) = q.get()
        for adj in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
            nx, ny = x + adj[0], y + adj[1]
            if nx < 0 or nx > maxX or ny < 0 or ny > maxY:
                continue

            nRisk = risk + riskLevelMap[nx, ny]

            if nx == maxX and ny == maxY:
                return nRisk

            if (nx, ny) in dists and dists[nx, ny] <= nRisk:
                continue

            dists[nx, ny] = nRisk
            q.put((nRisk, (nx, ny)))


def expandRiskLevelMap(riskLevelMap: 'dict[Tuple[int,int],int]') -> 'dict[Tuple[int,int],int]':
    maxX = max(x for x, _ in riskLevelMap.keys())
    maxY = max(y for y, _ in riskLevelMap.keys())

    expanded = riskLevelMap.copy()

    keys = list(expanded.keys())
    for xAdd in range(1, 5):
        for x, y in keys:
            expanded[x + (maxX + 1) * xAdd,
                     y] = (expanded[x, y] - 1 + xAdd) % 9 + 1

    keys = list(expanded.keys())
    for yAdd in range(1, 5):
        for x, y in keys:
            expanded[x, y + (maxY + 1) * yAdd] = (expanded[x,
                                                           y] - 1 + yAdd) % 9 + 1

    return expanded


def parseFile(lines: 'list[str]') -> 'dict[Tuple[int, int], int]':
    riskLevelMap: dict[Tuple[int, int], int] = {}
    for y, line in enumerate(lines):
        for x, risk in enumerate(line):
            riskLevelMap[x, y] = int(risk)
    return riskLevelMap


with open("15/input.txt", "r") as file:
    riskLevelMap = parseFile(lines=file.read().splitlines())
print(f"Lowest total risk path: {lowestRiskPath(riskLevelMap)}")
riskLevelMap = expandRiskLevelMap(riskLevelMap)
print(f"Task 2: {lowestRiskPath(riskLevelMap)}")
