def parseFile(input: str) -> 'dict[int, int]':
    lanternfishs: dict[int, int] = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    for lanternfish in input.split(","):
        lanternfishs[int(lanternfish)] += 1
    return lanternfishs


def simDays(lanternfishs: 'dict[int, int]', days: int) -> 'dict[int, int]':
    for day in range(days):
        newLanternfishs = lanternfishs[0]
        for key, value in lanternfishs.items():
            if key != 0:
                lanternfishs[key - 1] = value
        lanternfishs[6] += newLanternfishs
        lanternfishs[8] = newLanternfishs
    return lanternfishs


def sumLanternfishs(lanternfishs: 'dict[int, int]') -> int:
    sum = 0
    for num in lanternfishs.values():
        sum += num
    return sum


with open("6/input.txt", "r") as file:
    lanternfishs = parseFile(input=file.read().splitlines()[0])
t1 = 80
t2 = 256 - t1
simDays(lanternfishs, t1)
print(f"lanternfishs after {t1} days: {sumLanternfishs(lanternfishs)}")
simDays(lanternfishs, t2)
print(
    f"lanternfishs after another {t2} days: {sumLanternfishs(lanternfishs)}")
