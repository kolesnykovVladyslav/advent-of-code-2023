import re
import time
from collections import defaultdict

width = 101
height = 103
# width = 11
# height = 7
middle_x = width // 2
middle_y = height // 2


def get_input(line):
    pattern = "(-?\d+)"
    return [int(n) for n in re.findall(pattern, line)]


def solve(lines):
    steps = 100
    quadrants = defaultdict(lambda: 0)
    for line in lines:
        x, y, dx, dy = get_input(line)

        x = (x + dx * steps) % width
        y = (y + dy * steps) % height

        if x == middle_x or y == middle_y:
            continue

        quadrants[int(x > middle_x), int(y > middle_y)] += 1

    result = 1
    for value in quadrants.values():
        result *= value
    print(result)


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        solve(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
