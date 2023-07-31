import math

with open("input.txt") as f:
    raw_input = f.read().strip()


def main(input):
    crab_pos = [int(str) for str in input.split(",")]
    crab_pos.sort()
    median = crab_pos[math.floor(len(crab_pos) / 2)]
    fuel_used = sum(abs(crab - median) for crab in crab_pos)
    print(fuel_used)


main(raw_input)
