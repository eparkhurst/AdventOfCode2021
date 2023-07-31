with open("input.txt") as f:
    raw_input = f.read().strip()


def main(input):
    l_fish = [int(str) for str in input.split(",")]
    base_dict = {}
    for i in range(9):
        base_dict[i] = 0

    fish_dict = base_dict.copy()
    for fish in l_fish:
        fish_dict[fish] += 1

    for day in range(256):
        next_dict = base_dict.copy()
        for day in fish_dict:
            if day == 0:
                next_dict[6] += fish_dict[day]
                next_dict[8] = fish_dict[day]
            else:
                next_dict[day - 1] += fish_dict[day]
        fish_dict = next_dict
    count = 0
    for day in fish_dict:
        count += fish_dict[day]


main(raw_input)
