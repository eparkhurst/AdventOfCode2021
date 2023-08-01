with open("input.txt") as f:
    raw_input = f.read().strip().split("\n")


def main(input):
    count = 0
    for line in input:
        __, values = line.split("|")
        val_arr = values.split()
        for val in val_arr:
            char_len = len(val)
            if char_len == 2 or char_len == 3 or char_len == 4 or char_len == 7:
                count += 1
    print(count)


main(raw_input)
