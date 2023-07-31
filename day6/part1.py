with open("input.txt") as f:
    raw_input = f.read().strip()


def main(input):
    l_fish = [int(str) for str in input.split(",")]
    for day in range(80):
        next_fish = []
        for fish in l_fish:
            fish_day = fish - 1
            if fish_day < 0:
                fish_day = 6
                next_fish.append(8)
            next_fish.append(fish_day)
        l_fish = next_fish
    print(len(l_fish))


main(raw_input)
