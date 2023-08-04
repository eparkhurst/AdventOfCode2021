with open("input.txt") as f:
    raw_input = f.read().strip().split("\n")


char_values = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def check_corruption(line):
    openers = ["<", "(", "[", "{"]
    pairs = {
        ">": "<",
        ")": "(",
        "]": "[",
        "}": "{",
    }
    r_pairs = {
        "<": ">",
        "(": ")",
        "[": "]",
        "{": "}",
    }
    open_chars = []
    for char in line:
        if char in openers:
            open_chars.append(char)
        else:
            if open_chars.pop() != pairs[char]:
                return None
    return [r_pairs[x] for x in open_chars[::-1]]


def main(input):
    line_scores = []

    for line in input:
        ramainder = check_corruption(line)
        if not ramainder:
            continue
        score = 0
        for char in ramainder:
            score = score * 5
            score += char_values[char]
        line_scores.append(score)
    middle_index = int((len(line_scores) - 1) / 2)
    sort_scores = sorted(line_scores)
    print(sort_scores[middle_index])


main(raw_input)
