import time
from collections import defaultdict

width = 0
height = 0


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
    return 0 <= pos[0] < width and 0 <= pos[1] < height


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

    cheats = get_all_cheats(cell_to_dist, path, walls)

    number_of_cheats = sum([cheats[cheat] for cheat in cheats if cheat >= 100])
    print(number_of_cheats)
    # for cheat in cheats:
    #    print(f"There are {cheats[cheat]} cheats that save {cheat} picoseconds")


def get_all_cheats(cell_to_dist, path, walls):
    cheats = defaultdict(lambda: 0)
    for pos in path:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (pos[0] + dx, pos[1] + dy) not in walls:
                continue
            new_pos = (pos[0] + dx * 2, pos[1] + dy * 2)
            if pos_in_bounds(new_pos) and new_pos not in walls and cell_to_dist[new_pos] > cell_to_dist[pos]:
                diff = cell_to_dist[new_pos] - cell_to_dist[pos] - 2
                cheats[diff] += 1
    return cheats


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        solve(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
