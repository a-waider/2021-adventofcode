file = open("2/input.txt", "r")
lines = file.readlines()
file.close()

totalHorizontal = 0
totalDepth = 0
# Part 1
for line in lines:
    factor = int(''.join(c for c in line if c.isdigit()))
    if "forward" in line:
        totalHorizontal += factor
    elif "down" in line:
        totalDepth += factor
    elif "up" in line:
        totalDepth -= factor

print(f"total horizontal: {totalHorizontal}")
print(f"total depth: {totalDepth}")
print(f"multiplied result: {totalHorizontal * totalDepth}")

# Part 2
totalHorizontal = 0
totalDepth = 0
aim = 0
for line in lines:
    factor = int(''.join(c for c in line if c.isdigit()))
    if "forward" in line:
        totalHorizontal += factor
        totalDepth += factor * aim
    elif "down" in line:
        aim += factor
    elif "up" in line:
        aim -= factor

print(f"total horizontal: {totalHorizontal}")
print(f"total depth: {totalDepth}")
print(f"multiplied result: {totalHorizontal * totalDepth}")
