with open("input.txt") as f:
    raw_input = f.read().strip().split("\n")


def make_graph(input):
    graph = {}
    for line in input:
        cave1, cave2 = line.split("-")
        graph[cave1] = graph.get(cave1, []) + [cave2]
        graph[cave2] = graph.get(cave2, []) + [cave1]
    return graph


def recur(graph, node, visited):
    if node == "end":
        return 1
    if node in visited:
        return 0
    if not node.isupper():
        visited.append(node)
    count = 0
    for neighbor in graph[node]:
        new_list = visited.copy()
        count += recur(graph, neighbor, new_list)
    return count


def main(input):
    graph = make_graph(input)
    final = recur(graph, "start", [])
    print(final)


main(raw_input)
