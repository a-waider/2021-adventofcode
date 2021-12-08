from typing import Tuple
from math import pow


class SevenSegmentDisplay:
    def __init__(self, corruptedSignalPatterns: 'list[str]', corruptedDigets: 'list[int]') -> None:
        self.corruptedSignalPatterns = corruptedSignalPatterns
        self.corruptedDigets = corruptedDigets
        self.correctSignalPatterns = {
            0: "",
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: "",
            9: "",
        }


def parseFile(input: 'list[str]') -> None:
    sevenSegmentNumbers = []
    for line in input:
        signalPatterns = []
        for signalPattern in line.split(" | ")[0].split(" "):
            signalPatterns.append(signalPattern)
        sevenSegmentNumbers.append(SevenSegmentDisplay(
            signalPatterns, line.split(" | ")[1].split(" ")))
    return sevenSegmentNumbers


def getSimpleNumbersCount(sevenSegmentNumbers: 'list[SevenSegmentDisplay]') -> int:
    simpleNumbersCount = 0
    for sevenSegmentNumber in sevenSegmentNumbers:
        for corruptedDiget in sevenSegmentNumber.corruptedDigets:
            if len(corruptedDiget) == 2:  # Number 1
                simpleNumbersCount += 1
            elif len(corruptedDiget) == 3:  # Number 7
                simpleNumbersCount += 1
            elif len(corruptedDiget) == 4:  # Number 4
                simpleNumbersCount += 1
            elif len(corruptedDiget) == 7:  # Number 8
                simpleNumbersCount += 1
    return simpleNumbersCount


def decodeCorruptedSignalPatterns(sevenSegmentNumbers: 'list[SevenSegmentDisplay]') -> None:
    def difference(num1: str, num2: str) -> int:
        difference = 0
        for char in num1:
            if char not in num2:
                difference += 1
        return difference

    def twoOrFive(twoOrFive: 'list[str]', bottomAndBottomLeftSegments: str) -> 'Tuple[str, str, str, str]':
        # Found 2
        if bottomAndBottomLeftSegments[0] in twoOrFive[0] and bottomAndBottomLeftSegments[1] in twoOrFive[0]:
            bottomLeftSegment = bottomAndBottomLeftSegments
            for char in twoOrFive[1]:
                bottomLeftSegment = bottomLeftSegment.replace(char, "")
            bottomSegment = bottomAndBottomLeftSegments.replace(
                bottomLeftSegment, "")
            two = twoOrFive[0]
            five = twoOrFive[1]
        else:  # Found 5
            bottomLeftSegment = bottomAndBottomLeftSegments
            for char in twoOrFive[0]:
                bottomLeftSegment = bottomLeftSegment.replace(char, "")
            bottomSegment = bottomAndBottomLeftSegments.replace(
                bottomLeftSegment, "")
            two = twoOrFive[1]
            five = twoOrFive[0]
        return bottomSegment, bottomLeftSegment, two, five

    for sevenSegmentNumber in sevenSegmentNumbers:
        len5corruptedSignalPatterns = []
        for corruptedSignalPattern in sevenSegmentNumber.corruptedSignalPatterns:
            if len(corruptedSignalPattern) == 2:  # Number 1
                sevenSegmentNumber.correctSignalPatterns[1] = "".join(
                    sorted(corruptedSignalPattern))
            elif len(corruptedSignalPattern) == 3:  # Number 7
                sevenSegmentNumber.correctSignalPatterns[7] = "".join(
                    sorted(corruptedSignalPattern))
            elif len(corruptedSignalPattern) == 4:  # Number 4
                sevenSegmentNumber.correctSignalPatterns[4] = "".join(
                    sorted(corruptedSignalPattern))
            elif len(corruptedSignalPattern) == 7:  # Number 8
                sevenSegmentNumber.correctSignalPatterns[8] = "".join(
                    sorted(corruptedSignalPattern))
            elif len(corruptedSignalPattern) == 5:
                len5corruptedSignalPatterns.append(corruptedSignalPattern)

        # Get top segment
        for char in sevenSegmentNumber.correctSignalPatterns[7]:
            if char not in sevenSegmentNumber.correctSignalPatterns[1]:
                topSegment = char

        # Get right segments
        rightSegments = sevenSegmentNumber.correctSignalPatterns[1]

        # Get bottom and bottomLeft segments
        bottomAndBottomLeftSegments = "abcdefg"
        bottomAndBottomLeftSegments = bottomAndBottomLeftSegments.replace(
            topSegment, "")
        for char in sevenSegmentNumber.correctSignalPatterns[4]:
            bottomAndBottomLeftSegments = bottomAndBottomLeftSegments.replace(
                char, "")

        # Get center and topLeft segment
        centerAndTopLeftSegments = sevenSegmentNumber.correctSignalPatterns[4]
        for char in sevenSegmentNumber.correctSignalPatterns[1]:
            centerAndTopLeftSegments = centerAndTopLeftSegments.replace(
                char, "")

        # Separate bottomSegment and bottomLeftSegment
        if difference(len5corruptedSignalPatterns[0], len5corruptedSignalPatterns[1]) == 2:
            bottomSegment, bottomLeftSegment, two, five = twoOrFive([
                len5corruptedSignalPatterns[0],
                len5corruptedSignalPatterns[1]
            ], bottomAndBottomLeftSegments)
            three = len5corruptedSignalPatterns[2]
        elif difference(len5corruptedSignalPatterns[1], len5corruptedSignalPatterns[2]) == 2:
            bottomSegment, bottomLeftSegment, two, five = twoOrFive([
                len5corruptedSignalPatterns[1],
                len5corruptedSignalPatterns[2],
                bottomAndBottomLeftSegments
            ], bottomAndBottomLeftSegments)
            three = len5corruptedSignalPatterns[0]
        elif difference(len5corruptedSignalPatterns[0], len5corruptedSignalPatterns[2]) == 2:
            bottomSegment, bottomLeftSegment, two, five = twoOrFive([
                len5corruptedSignalPatterns[0],
                len5corruptedSignalPatterns[2]
            ], bottomAndBottomLeftSegments)

        # Get top left segment
        topLeftSegment = centerAndTopLeftSegments
        for char in two:
            topLeftSegment = topLeftSegment.replace(char, "")

        # Get center segment
        centerSegment = centerAndTopLeftSegments.replace(topLeftSegment, "")

        # Get top right segment
        topRightSegment = rightSegments
        for char in five:
            topRightSegment = topRightSegment.replace(char, "")

        # Get bottom right segment
        bottomRightSegment = rightSegments.replace(topRightSegment, "")

        sevenSegmentNumber.correctSignalPatterns[0] = "".join(sorted(topSegment + topRightSegment +
                                                                     bottomRightSegment + bottomSegment + bottomLeftSegment + topLeftSegment))
        sevenSegmentNumber.correctSignalPatterns[2] = "".join(sorted(topSegment + topRightSegment +
                                                                     centerSegment + bottomLeftSegment + bottomSegment))
        sevenSegmentNumber.correctSignalPatterns[3] = "".join(sorted(topSegment + topRightSegment +
                                                                     centerSegment + bottomRightSegment + bottomSegment))
        sevenSegmentNumber.correctSignalPatterns[5] = "".join(sorted(topSegment + topLeftSegment +
                                                                     centerSegment + bottomRightSegment + bottomSegment))
        sevenSegmentNumber.correctSignalPatterns[6] = "".join(sorted(topSegment + topLeftSegment +
                                                                     centerSegment + bottomLeftSegment + bottomRightSegment + bottomSegment))
        sevenSegmentNumber.correctSignalPatterns[9] = "".join(sorted(topSegment + topLeftSegment +
                                                                     topRightSegment + centerSegment + bottomRightSegment + bottomSegment))


def numbersSum(sevenSegmentNumbers: 'list[SevenSegmentDisplay]') -> int:
    sum = 0
    for sevenSegmentNumber in sevenSegmentNumbers:
        for i, corruptedDiget in enumerate(sevenSegmentNumber.corruptedDigets):
            for j, signalPattern in enumerate(list(sevenSegmentNumber.correctSignalPatterns.values())):
                if signalPattern == "".join(sorted(corruptedDiget)):
                    sum += j*pow(10, 3-i)
    return int(sum)


with open("8/input.txt", "r") as file:
    input = parseFile(input=file.read().splitlines())
simpleNumbersCount = getSimpleNumbersCount(input)
print(f"simple numbers count (1, 4, 7, 8): {simpleNumbersCount}")
decodeCorruptedSignalPatterns(input)
print(f"decoded numbers sum: {numbersSum(input)}")
