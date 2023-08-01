with open("input.txt") as f:
    raw_input = f.read().strip().split("\n")

num_key = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def get_sig_map(signals):
    sig_map = {}
    sig_arr = signals.split()
    counts = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}
    one, seven, four, eight = None, None, None, None
    for sig in sig_arr:
        if len(sig) == 2:
            one = sig
        if len(sig) == 3:
            seven = sig
        if len(sig) == 4:
            four = sig
        if len(sig) == 7:
            eight = sig
        for char in sig:
            counts[char] += 1
    for char in seven:
        if char not in one:
            sig_map["a"] = char
    for key in counts:
        if counts[key] == 9:
            sig_map["f"] = key
        if counts[key] == 4:
            sig_map["e"] = key
        if counts[key] == 6:
            sig_map["b"] = key
    one_e = one + sig_map["b"]
    for char in four:
        if char not in one_e:
            sig_map["d"] = char

    for char in one:
        if char != sig_map["f"]:
            sig_map["c"] = char
    so_far = "".join(sig_map.values())
    for char in eight:
        if char not in so_far:
            sig_map["g"] = char
    swapped = {v: k for k, v in sig_map.items()}
    return swapped


def main(input):
    count = 0
    for line in input:
        singals, values = line.split("|")
        sig_map = get_sig_map(singals)
        str_num = ""
        for val in values.split():
            num_string = ""
            for char in val:
                num_string += str(sig_map[char])
            all_letters = "".join(sorted(num_string))
            num = num_key[all_letters]
            str_num += num
        count += int(str_num)
    print(count)


main(raw_input)
