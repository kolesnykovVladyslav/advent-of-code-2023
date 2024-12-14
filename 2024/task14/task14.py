import re
import sys
import time
from collections import defaultdict

f = open("output.txt", 'w')
width = 101
height = 103
# width = 11
# height = 7
middle_x = width // 2
middle_y = height // 2


def get_input(line):
    pattern = "(-?\d+)"
    return [int(n) for n in re.findall(pattern, line)]


def solve1(lines):
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


def print_map(robots):
    pos = set([(robot[0], robot[1]) for robot in robots])
    for i in range(width):
        line = ""
        for j in range(height):
            if (i, j) in pos:
                line += "R"
            else:
                line += "."
        f.write(line)


def solve2(lines):
    # 6000
    initial_steps = 6000
    steps = 1000
    robots = []
    for line in lines:
        robots.append(get_input(line))

    # initial pos
    for robot in robots:
        x, y, dx, dy = robot

        x = (x + dx * initial_steps) % width
        y = (y + dy * initial_steps) % height
        robot[0] = x
        robot[1] = y

    min_distance = sys.maxsize
    min_step = 0
    final_pos = []
    for step in range(steps):
        distance = 0
        for robot in robots:
            x, y, dx, dy = robot
            x = (x + dx) % width
            y = (y + dy) % height
            robot[0] = x
            robot[1] = y
            distance += get_distance_to_all(x, y, robots)
        f.write(
            "\n----------------------------------" + str(step + initial_steps) + "----------------------------------\n")
        print_map(robots)
        distance = distance / len(robots)
        if distance < min_distance:
            min_distance = distance
            min_step = initial_steps + step
            final_pos = robots.copy()
        # print()
        # print("----------------------------------" + str(step) + "----------------------------------")
        # print_map(robots)
    print(min_step, min_distance)
    print_map(final_pos)


def get_distance_to_all(x, y, robots):
    dist = 0
    for robot in robots:
        dist += abs(robot[0] - x) + abs(robot[1] - y)
    return dist / len(robots)


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        # solve1(lines)
        solve2(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
