from collections import deque

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


# bfs
def get_basin(x, y, matrix):
    count = 0
    visited = set()
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if get_point(x, y, matrix) < 9:
            count += 1
            q.append((x - 1, y))
            q.append((x + 1, y))
            q.append((x, y - 1))
            q.append((x, y + 1))
    return count


def get_minima(matrix):
    basins = []
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
                basin = get_basin(x, y, matrix)
                basins.append(basin)

    return basins


def main(input):
    matrix = []
    for line in input:
        chars = [*line]
        matrix.append([int(c) for c in chars])
    basins = sorted(get_minima(matrix))
    largest = basins[-3:]
    total = 1
    for i in largest:
        total *= i
    print(total)


main(raw_input)
