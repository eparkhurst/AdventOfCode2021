with open("input.txt") as f:
    raw_input = f.read().strip()


def count_dict(
    dot_dict,
):
    count = 0
    for y in dot_dict:
        dot_set = set(dot_dict[y])
        count += len(dot_set)
    print(count)


def get_dot_dict(dots):
    dot_dict = {}
    for dot in dots:
        x, y = dot.split(",")
        dot_dict[y] = dot_dict.get(y, []) + [x]
    return dot_dict


def fold_paper(dot_dict, folds):
    final_y, final_x = 0, 0
    fold = folds[0]
    _, eq = fold.split("fold along ")
    dir, val = eq.split("=")
    if dir == "x":
        final_x = int(val)
        for y in dot_dict:
            next = []
            for x in dot_dict[y]:
                if int(x) < int(val):
                    next.append(int(x))
                else:
                    next.append(int(val) - (int(x) - int(val)))
            dot_dict[y] = next
    else:
        final_y = int(val)
        next_dict = {}
        for key in dot_dict:
            if int(key) > int(val):
                next_y = str(int(val) - (int(key) - int(val)))
                next_dict[next_y] = dot_dict.get(next_y, []) + dot_dict[key]
            else:
                next_dict[key] = next_dict.get(key, []) + dot_dict[key]
        dot_dict = next_dict
    return (dot_dict, final_x, final_y)


def main(input):
    dots, folds = input.split("\n\n")
    dots = dots.split("\n")
    folds = folds.split("\n")
    dot_dict = get_dot_dict(dots)
    final_dict, x, y = fold_paper(dot_dict, folds)

    count_dict(final_dict)


main(raw_input)
