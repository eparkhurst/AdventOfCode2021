with open("input.txt") as f:
    raw_input = f.read().strip().split("\n")


def get_point(y, x, matrix):
    if x < 0 or y < 0:
        return -1
    try:
        point = matrix[y][x]
        return point
    except IndexError:
        return -1


def check_matrix(octs):
    for row in octs:
        for oct in row:
            if oct > 9:
                return True
    return False


def reset_octs(next_step):
    count = 0
    for y, row in enumerate(next_step):
        for x, oct in enumerate(row):
            if oct > 9:
                next_step[y][x] = 0
                count += 1
                if get_point(y, x - 1, next_step) > 0:
                    next_step[y][x - 1] += 1
                if get_point(y, x + 1, next_step) > 0:
                    next_step[y][x + 1] += 1
                if get_point(y - 1, x, next_step) > 0:
                    next_step[y - 1][x] += 1
                if get_point(y + 1, x, next_step) > 0:
                    next_step[y + 1][x] += 1
                if get_point(y - 1, x - 1, next_step) > 0:
                    next_step[y - 1][x - 1] += 1
                if get_point(y + 1, x + 1, next_step) > 0:
                    next_step[y + 1][x + 1] += 1
                if get_point(y - 1, x + 1, next_step) > 0:
                    next_step[y - 1][x + 1] += 1
                if get_point(y + 1, x - 1, next_step) > 0:
                    next_step[y + 1][x - 1] += 1
    return (next_step, count)


def run_step(octs):
    step_count = 0
    next_step = []
    for row in octs:
        next_step.append([x + 1 for x in row])

    while check_matrix(next_step):
        next_step, count = reset_octs(next_step)
        step_count += count

    return (next_step, step_count)


def main(input):
    octs = []
    final_count = 0
    for line in input:
        num_line = [int(x) for x in line]
        octs.append(num_line)

    for i in range(100):
        octs, count = run_step(octs)
        final_count += count
    print(final_count)


main(raw_input)
