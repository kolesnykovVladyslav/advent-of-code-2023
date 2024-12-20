import time
from collections import defaultdict

width = 0
height = 0
input_file = 'input.txt'
at_least_dist = 100
at_most_cheats = 20


def get_input(lines):
    global width, height
    width = len(lines[0]) - 1
    height = len(lines)
    walls = set()
    initial_pos = None
    finish_pos = None
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "\n":
                continue
            if char == "#":
                walls.add((x, y))
            if char == "S":
                initial_pos = (x, y)
            if char == "E":
                finish_pos = (x, y)
    return walls, initial_pos, finish_pos


def pos_in_bounds(pos):
    return 0 < pos[0] < width and 0 < pos[1] < height


def solve(lines):
    walls, start, finish = get_input(lines)
    path = list()
    cell_to_dist = defaultdict(lambda: -1)
    cell_to_dist[start] = 0

    queue = [start]
    while len(queue) > 0:
        pos = queue.pop(0)
        path.append(pos)
        dist = cell_to_dist[pos]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = (pos[0] + dx, pos[1] + dy)
            if new_pos not in walls and pos_in_bounds(new_pos) and new_pos not in cell_to_dist:
                cell_to_dist[new_pos] = dist + 1
                queue.append(new_pos)

    cheats = get_all_cheats(cell_to_dist, path)
    number_of_cheats = sum([cheats[cheat] for cheat in cheats if cheat >= at_least_dist])

    for cheat in sorted(cheats):
        if cheat < at_least_dist:
            continue
        print(f"There are {cheats[cheat]} cheats that save {cheat} picoseconds")
    print(number_of_cheats)


def get_all_cheats(cell_to_dist, path):
    cheats = defaultdict(lambda: 0)
    for i, pos1 in enumerate(path):
        for pos2 in path[i + 2:]:
            dist = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
            if dist > at_most_cheats or cell_to_dist[pos2] - cell_to_dist[pos1] < at_least_dist:
                continue

            diff = cell_to_dist[pos2] - cell_to_dist[pos1] - dist
            cheats[diff] += 1
    return cheats


if __name__ == "__main__":
    start_time = time.time()
    with open(input_file, 'r') as file:
        lines = file.readlines()
        solve(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
