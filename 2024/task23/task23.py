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


def bron_kerbosch(R, P, X, graph, cliques):
    if not P and not X:
        cliques.append(R)
        return
    for v in list(P):
        bron_kerbosch(R.union([v]), P.intersection(graph[v]), X.intersection(graph[v]), graph, cliques)
        P.remove(v)
        X.add(v)


def find_largest_clique(graph):
    cliques = []
    bron_kerbosch(set(), set(graph.keys()), set(), graph, cliques)
    largest_clique = max(cliques, key=len)
    return largest_clique


def generate_password(clique):
    sorted_clique = sorted(clique)
    password = ",".join(sorted_clique)
    return password


def solve2(lines):
    connections = parse_input(lines)
    graph = build_graph(connections)
    largest_clique = find_largest_clique(graph)
    password = generate_password(largest_clique)
    print(password)


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        solve(lines)
        solve2(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
