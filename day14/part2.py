import math

with open("input.txt") as f:
    raw_input = f.read().strip()


def get_counts(countDict):
    counts = {}
    for pair in countDict:
        if pair[0] not in counts:
            counts[pair[0]] = countDict[pair] / 2
        else:
            counts[pair[0]] += countDict[pair] / 2
        if pair[1] not in counts:
            counts[pair[1]] = countDict[pair] / 2
        else:
            counts[pair[1]] += countDict[pair] / 2
    return counts


def main(input):
    start, rules = input.split("\n\n")
    rules = rules.split("\n")
    rule_dict = {}
    for rule in rules:
        pair, result = rule.split(" -> ")
        rule_dict[pair] = result

    count_dict = rule_dict.copy()
    for key in count_dict:
        count_dict[key] = 0

    for j in range(len(start)):
        if j == len(start) - 1:
            continue
        else:
            pair = start[j : j + 2]
            count_dict[pair] += 1

    for i in range(40):
        new_count_dict = count_dict.copy()
        for key in rule_dict:
            middle = rule_dict[key]
            new_count_dict[key] -= count_dict.get(key, 0)
            new_count_dict[key[0] + middle] += count_dict[key]
            new_count_dict[middle + key[1]] += count_dict[key]
        count_dict = new_count_dict
    counts = get_counts(count_dict)

    sorted_counts = [math.ceil(x) for x in sorted(counts.values())]
    print(sorted_counts[-1] - sorted_counts[0])


main(raw_input)
