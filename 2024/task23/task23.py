import time


def parse_input(lines):
    connections = [line.strip().split('-') for line in lines]
    return connections


def build_graph(connections):
    from collections import defaultdict
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)
    return graph


def find_triangles(graph):
    triangles = set()
    sorted_graph = [node for node in graph if node.startswith('t')]
    for node in sorted_graph:
        neighbors = graph[node]
        for neighbor in neighbors:
            mutual = neighbors.intersection(graph[neighbor])
            for third in mutual:
                triangle = tuple(sorted([node, neighbor, third]))
                triangles.add(triangle)
    return triangles


def solve(lines):
    connections = parse_input(lines)
    graph = build_graph(connections)
    triangles = find_triangles(graph)
    print(len(triangles))


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        solve(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
