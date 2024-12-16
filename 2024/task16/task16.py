import enum
import sys
import time
from collections import defaultdict


class Direction(enum.Enum):
    up = (0, -1)
    left = (-1, 0)
    down = (0, 1)
    right = (1, 0)


def turn_clockwise(value: Direction):
    if value == Direction.up:
        return Direction.right
    elif value == Direction.right:
        return Direction.down
    elif value == Direction.down:
        return Direction.left
    elif value == Direction.left:
        return Direction.up


def get_input(lines):
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
    return walls, initial_pos, finish_pos, width, height


def solve1(lines):
    walls, initial_pos, finish_pos, width, height = get_input(lines)

    score_of_cells = defaultdict(lambda: sys.maxsize)
    visited_cells_path = defaultdict(lambda: set())
    score_of_cells[(initial_pos, Direction.right)] = 0
    score_of_cells[(initial_pos, Direction.up)] = 1000
    queue = [(initial_pos, Direction.right), (initial_pos, Direction.up)]

    while len(queue) > 0:
        pos, direction = queue.pop(0)
        score = score_of_cells[(pos, direction)]
        visited_cells_path[(pos, direction)].add(pos)
        if pos == finish_pos:
            continue
        new_pos = (pos[0] + direction.value[0], pos[1] + direction.value[1])
        if new_pos in walls:
            continue

        for dir, rotate_price in [(direction, 0),
                                  (turn_clockwise(direction), 1000),
                                  (turn_clockwise(turn_clockwise(turn_clockwise(direction))), 1000)]:

            new_score = score + rotate_price + 1
            if score_of_cells[(new_pos, dir)] > new_score:
                score_of_cells[(new_pos, dir)] = new_score
                visited_cells_path[(new_pos, dir)] = visited_cells_path[(pos, direction)].copy()
                queue.append((new_pos, dir))
            elif score_of_cells[(new_pos, dir)] == new_score:
                visited_cells_path[(new_pos, dir)].update(visited_cells_path[(pos, direction)])
                queue.append((new_pos, dir))

    lowest_score = min(score_of_cells[finish_pos, Direction.up], score_of_cells[finish_pos, Direction.right])
    print(lowest_score)
    print(len(visited_cells_path[finish_pos, Direction.up]))
    print_map(finish_pos, height, visited_cells_path, walls, width)


def print_map(finish_pos, height, visited_cells_path, walls, width):
    for y in range(height):
        line = ""
        for x in range(width):
            if (x, y) in visited_cells_path[finish_pos, Direction.up]:
                line += "0"
            elif (x, y) in walls:
                line += "#"
            else:
                line += "."
        print(line)


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        solve1(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
