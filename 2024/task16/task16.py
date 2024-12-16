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

    visited_cells = defaultdict(lambda: sys.maxsize)
    visited_cells[initial_pos] = 0
    queue = [(initial_pos, Direction.right)]

    while len(queue) > 0:
        pos, direction = queue.pop()
        score = visited_cells.get(pos)

        for dir, rotate_price in [(direction, 0),
                                  (turn_clockwise(direction), 1000),
                                  (turn_clockwise(turn_clockwise(direction)), 2000),
                                  (turn_clockwise(turn_clockwise(turn_clockwise(direction))), 1000)]:
            new_pos = (pos[0] + dir.value[0], pos[1] + dir.value[1])
            if new_pos in walls:
                continue

            new_score = score + rotate_price + 1
            if visited_cells[new_pos] > new_score:
                visited_cells[new_pos] = new_score
                if new_pos != finish_pos:
                    queue.append((new_pos, dir))

    print(visited_cells[finish_pos])


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        solve1(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
