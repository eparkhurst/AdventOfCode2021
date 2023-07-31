with open("input.txt") as f:
    input = f.read().strip().split("\n")


def format_input(input):
    formatted_array = []
    for ln in input:
        start, end = ln.split(" -> ")
        formatted_array.append([start.split(","), end.split(",")])
    return formatted_array


def add_to_map(map, x, y):
    if x not in map:
        map[x] = {}
    if y not in map[x]:
        map[x][y] = 0
    map[x][y] += 1
    return map


def fill_map(coords):
    map = {}
    for line in coords:
        start, end = line
        start_x, start_y = start
        if start_x == end[0]:
            y_pos = int(start_y)

            while y_pos != int(end[1]):
                add_to_map(map, int(start_x), y_pos)
                if y_pos < int(end[1]):
                    y_pos += 1
                else:
                    y_pos -= 1
            add_to_map(map, int(start_x), y_pos)

        if start_y == end[1]:
            x_pos = int(start_x)

            while x_pos != int(end[0]):
                add_to_map(map, x_pos, int(start_y))
                if x_pos < int(end[0]):
                    x_pos += 1
                else:
                    x_pos -= 1
            add_to_map(map, x_pos, int(start_y))
    return map


def count_map(map):
    count = 0
    for x in map:
        for y in map[x]:
            if map[x][y] > 1:
                count += 1
    return count


def main(input):
    coords = format_input(input)
    map = fill_map(coords)

    print(count_map(map))


main(input)
