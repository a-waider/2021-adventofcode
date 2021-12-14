from typing import Tuple
from collections import Counter


def simSteps(polymerTemplate: str, polymerRules: 'dict[str,str]', steps: int) -> str:
    pairs = Counter()
    chars = Counter(polymerTemplate)

    for runningCounter in range(1, len(polymerTemplate)):
        pair = polymerTemplate[runningCounter-1:runningCounter+1]
        pairs[pair] += 1

    for _ in range(steps):
        tmp = Counter()
        for pair, count in pairs.items():
            if pair in polymerRules:
                tmp[pair[0] + polymerRules[pair]] += count
                tmp[polymerRules[pair] + pair[1]] += count
                chars[polymerRules[pair]] += count
        pairs = tmp

    return max(list(chars.values())) - min(list(chars.values()))


def parseFile(lines: 'list[str]') -> Tuple[int, 'dict[str, str]']:
    polymerTemplate = lines[0]
    polymerRules: dict[str, str] = {}
    for line in lines[2:]:
        polymerRules[line.split(" -> ")[0]] = line.split(" -> ")[1]
    return polymerTemplate, polymerRules


with open("14/input.txt", "r") as file:
    polymerTemplate, polymerRules = parseFile(lines=file.read().splitlines())
print(f"Task 1: {simSteps(polymerTemplate, polymerRules, 10)}")
print(f"Task 2: {simSteps(polymerTemplate, polymerRules, 40)}")
