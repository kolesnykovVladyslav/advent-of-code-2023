import sys
import time
from collections import defaultdict

# bytes = 12
bytes = 1024
width, height = 70, 70


# width, height = 6, 6


def get_input(lines):
    input = set()
    for i in range(bytes):
        a, b = lines[i].strip().split(',')
        input.add((int(a), int(b)))
    return input


def pos_in_bounds(pos):
    return 0 <= pos[0] <= width and 0 <= pos[1] <= height


def solve(lines):
    walls = get_input(lines)
    start = (0, 0)
    score_of_cells = defaultdict(lambda: sys.maxsize)
    score_of_cells[start] = 0

    queue = [start]
    while len(queue) > 0:
        pos = queue.pop(0)
        score = score_of_cells[pos]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pos = (pos[0] + dx, pos[1] + dy)
            new_score = score + 1
            if new_pos not in walls and pos_in_bounds(new_pos) and score_of_cells[new_pos] > new_score:
                score_of_cells[new_pos] = new_score
                queue.append(new_pos)
    finish = (width, height)
    print(score_of_cells[finish])
    for y in range(height + 1):
        line = ""
        for x in range(width + 1):
            if (x, y) in walls:
                line += "#"
            else:
                line += "."
        print(line)


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        solve(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
