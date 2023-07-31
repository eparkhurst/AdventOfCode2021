import math

with open("input.txt") as f:
    raw_input = f.read().strip()


def main(input):
    crab_pos = [int(str) for str in input.split(",")]
    crab_pos.sort()
    mean = math.floor(sum(crab_pos) / len(crab_pos))
    fuel = 0
    for crab in crab_pos:
        dif = abs(crab - mean)
        fuel += sum(range(1, dif + 1))
    print(fuel)


main(raw_input)
# 85015849 too high
