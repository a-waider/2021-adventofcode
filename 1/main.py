file = open("1/input.txt", "r")
lines = [int(i) for i in file.readlines()]
file.close()

previous = -1
current = None
totalIncreased = 0

# Part 1
for line in lines:
    current = int(line)
    if previous == -1:  # First value will be ignored
        pass
    elif current > previous:
        totalIncreased += 1
    previous = current
print(f"total increased: {totalIncreased}")

# Part 2
previous = -1
current = None
totalIncreased = 0
for i in range(len(lines)-2):
    current = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    if previous == -1:  # First value will be ignored
        pass
    elif current > previous:
        totalIncreased += 1
    previous = current
print(f"total increased: {totalIncreased}")
