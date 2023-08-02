with open("input.txt") as f:
    raw_input = f.read().strip().split("\n")


def get_point(x, y, matrix):
    if x < 0 or y < 0:
        return 10
    try:
        point = matrix[y][x]
        return point
    except IndexError:
        return 10


def get_minima(matrix):
    minima = []
    for y, row in enumerate(matrix):
        for x, point in enumerate(row):
            surrounding = []
            surrounding.append(get_point(x - 1, y, matrix))
            surrounding.append(get_point(x + 1, y, matrix))
            surrounding.append(get_point(x, y - 1, matrix))
            surrounding.append(get_point(x, y + 1, matrix))
            lowest_surrounding = min(surrounding)
            if point == lowest_surrounding and point < 9:
                print("how often?", point, x, y)
                print(row)
            if point < lowest_surrounding:
                minima.append(point)

    return minima


def main(input):
    matrix = []
    for line in input:
        chars = [*line]
        matrix.append([int(c) for c in chars])
    local_minima = get_minima(matrix)
    count = sum([x + 1 for x in local_minima])
    print(count)


main(raw_input)
# 1548 too high
# 535 too low
