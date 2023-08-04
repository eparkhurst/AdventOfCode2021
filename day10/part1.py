with open("input.txt") as f:
    raw_input = f.read().strip().split("\n")


char_values = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def check_corruption(line):
    openers = ["<", "(", "[", "{"]
    pairs = {
        ">": "<",
        ")": "(",
        "]": "[",
        "}": "{",
    }
    open_chars = []
    for char in line:
        if char in openers:
            open_chars.append(char)
        else:
            if open_chars.pop() != pairs[char]:
                return char
    return None


def main(input):
    char_count = {
        ">": 0,
        ")": 0,
        "]": 0,
        "}": 0,
    }

    for line in input:
        char = check_corruption(line)
        if char in char_count:
            char_count[char] += 1

    score = 0
    for char in char_count:
        score += char_count[char] * char_values[char]
    print(score)


main(raw_input)
