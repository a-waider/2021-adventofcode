class IncompleteError(Exception):
    def __init__(self, missingBrackets):
        self.missingBrackets = missingBrackets


def parseFile(input: 'list[str]') -> 'list[list[int]]':
    lines: 'list[str]' = []
    for line in input:
        lines.append(line)
    return lines


def evalLine(line: str) -> None:
    tree: list[str] = []
    opening = {"(": 0, "[": 1, "{": 2, "<": 3}
    closing = {")": 0, "]": 1, "}": 2, ">": 3}
    for item in line:
        if not tree:  # First bracket
            tree.append(item)
        else:
            if item in opening:
                tree.append(item)
            else:
                if opening[tree[len(tree)-1]] == closing[item]:
                    tree.pop()
                else:
                    raise SyntaxError(item)
    if len(tree) > 0:
        missingBrackets: list[str] = []
        for missingBracket in reversed(tree):
            for closingBracket in closing:
                if opening[missingBracket] == closing[closingBracket]:
                    missingBrackets.append(closingBracket)
        raise IncompleteError(missingBrackets)


def corruptedLines(lines: 'list[str]') -> int:
    syntaxErrorPoints = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    syntaxErrorScore = 0
    for line in lines:
        try:
            evalLine(line)
        except SyntaxError as e:
            syntaxErrorScore += syntaxErrorPoints[e.msg]
        except IncompleteError:
            pass
    return syntaxErrorScore


def incompleteLines(lines: 'list[str]') -> int:
    autocompletePoints = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    autocompleteScores: list[int] = []
    for line in lines:
        try:
            evalLine(line)
        except SyntaxError:
            pass
        except IncompleteError as e:
            autocompleteScore = 0
            for missingBracket in e.missingBrackets:
                autocompleteScore *= 5
                autocompleteScore += autocompletePoints[missingBracket]
            autocompleteScores.append(autocompleteScore)
    autocompleteScores = sorted(autocompleteScores)
    return autocompleteScores[int(len(autocompleteScores)/2)]


with open("10/input.txt", "r") as file:
    lines = parseFile(input=file.read().splitlines())
print(f"corrupted lines score: {corruptedLines(lines)}")
print(f"incomplete lines score: {incompleteLines(lines)}")
