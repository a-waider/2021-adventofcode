file = open("3/input.txt", "r")
lines = file.read().splitlines()
file.close()

# Part 1


def getStats(array: list) -> 'list[int]':
    zeros = [0]*len(array[0])
    ones = [0]*len(array[0])
    for item in array:
        for i, bit in enumerate(item):
            if int(bit) == 1:
                ones[i] += 1
            elif int(bit) == 0:
                zeros[i] += 1
    return zeros, ones


gamma = 0
epsilon = 0

zeros, ones = getStats(lines)
for i in range(len(ones)):
    gamma <<= 1
    if ones[i] > zeros[i]:
        gamma += 1
    epsilon <<= 1
    if ones[i] < zeros[i]:
        epsilon += 1


print(f"gamma: {gamma}")
print(f"epsilon: {epsilon}")
print(f"multiplied result: {gamma * epsilon}")

# Part 2


def filterList(array: list, type: bool) -> int:
    pos = 0
    while len(array) > 1:
        ones = []
        zeros = []
        for item in array:
            if int(item[pos]) == 1:
                ones.append(item)
            else:
                zeros.append(item)
        asdf = [zeros, ones]
        if type:
            array = [zeros, ones][len(ones) >= len(zeros)]
        else:
            array = [zeros, ones][len(ones) < len(zeros)]
        pos += 1
    return int(array[0], 2)


oxygen = filterList(lines.copy(), True)
co2 = filterList(lines.copy(), False)


print(f"oxygen: {oxygen}")
print(f"co2: {co2}")
print(f"life support: {oxygen * co2}")
