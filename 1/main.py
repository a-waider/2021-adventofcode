file = open("1/input.txt", "r")
lines = file.readlines()
file.close()

previous = -1
current = None
totalIncreased = 0

for line in lines:
    current = int(line)
    if previous == -1:  # First value will be ignored
        pass
    elif current > previous:
        totalIncreased += 1
    previous = current

print(f"total increased: {totalIncreased}")
