with open("input.txt") as f:
    content = f.read().strip().split("\n")


def get_common_binary_string(strings):
    counts = [0] * len(strings[0])

    for line in strings:
        for i, char in enumerate(line):
            counts[i] += int(char)

    half = len(strings) / 2
    gama = ""
    epsilon = ""
    for count in counts:
        if count >= half:
            gama += "1"
            epsilon += "0"
        else:
            gama += "0"
            epsilon += "1"
    return gama, epsilon


oxygen_rating = content
for i in range(0, len(content[0])):
    if len(oxygen_rating) == 1:
        break
    localG, localE = get_common_binary_string(oxygen_rating)
    oxygen_rating = list(filter(lambda line: line[i] == localG[i], oxygen_rating))

co2 = content
for i in range(0, len(content[0])):
    if len(co2) == 1:
        break
    localG, localE = get_common_binary_string(co2)
    co2 = list(filter(lambda line: line[i] == localE[i], co2))
print(int(oxygen_rating[0], 2) * int(co2[0], 2))
