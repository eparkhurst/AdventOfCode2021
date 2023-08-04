with open("input.txt") as f:
    raw_input = f.read().strip()


def get_counts(polymer):
    counts = {}
    for char in polymer:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts


def main(input):
    start, rules = input.split("\n\n")
    rules = rules.split("\n")
    rule_dict = {}
    for rule in rules:
        pair, result = rule.split(" -> ")
        rule_dict[pair] = result
    for i in range(10):
        new_start = ""
        for j in range(len(start)):
            if j == len(start) - 1:
                new_start += start[j]
            else:
                pair = start[j : j + 2]
                new_start += pair[0] + rule_dict.get(pair, "")
        start = new_start
    counts = get_counts(start)
    sorted_counts = sorted(counts.values())
    print(sorted_counts)
    print(sorted_counts[-1] - sorted_counts[0])


main(raw_input)
