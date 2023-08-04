with open("input.txt") as f:
    raw_input = f.read().strip().split("\n")


def make_graph(input):
    graph = {}
    for line in input:
        cave1, cave2 = line.split("-")
        graph[cave1] = graph.get(cave1, []) + [cave2]
        graph[cave2] = graph.get(cave2, []) + [cave1]
    return graph


def recur(graph, node, visited, twiced):
    if node == "end":
        return 1

    if node in visited and twiced:
        return 0
    if node in visited:
        if node == "start":
            return 0
        twiced = True
    elif not node.isupper():
        visited.append(node)

    count = 0
    for neighbor in graph[node]:
        new_list = visited.copy()
        count += recur(graph, neighbor, new_list, twiced)
    return count


def main(input):
    graph = make_graph(input)
    final = recur(graph, "start", [], False)
    print(final)


main(raw_input)
