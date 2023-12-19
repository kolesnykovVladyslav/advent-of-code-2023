import sys


def main():
    with open("input.txt") as f:
        lines = [l for l in f.read().splitlines()]
        solve_a(lines)


def solve_a(lines):
    min_x, min_y = sys.maxsize, sys.maxsize
    max_x, max_y = -sys.maxsize, -sys.maxsize
    coordinate = (0, 0)
    path = set()
    path.add(coordinate)
    for line in lines:
        direction, meters, rgb = line.split()

        dx, dy = 0, 0
        if direction == "R":
            dx, dy = 1, 0
        elif direction == "L":
            dx, dy = -1, 0
        elif direction == "U":
            dx, dy = 0, -1
        elif direction == "D":
            dx, dy = 0, 1

        for _ in range(1, int(meters) + 1):
            new_x, new_y = coordinate[0] + dx, coordinate[1] + dy
            coordinate = (new_x, new_y)
            path.add(coordinate)

            min_x = min(min_x, new_x)
            min_y = min(min_y, new_y)
            max_x = max(max_x, new_x)
            max_y = max(max_y, new_y)

    # outer cells
    seen = set()
    queue = [(min_x - 1, min_y - 1)]

    while queue:
        coordinate = queue.pop()
        if coordinate in seen or coordinate in path:
            continue
        seen.add(coordinate)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_coordinate = (coordinate[0] + dx, coordinate[1] + dy)
            if min_x - 1 <= next_coordinate[0] <= max_x + 1 and min_y - 1 <= next_coordinate[1] <= max_y + 1:
                queue.append(next_coordinate)

    cubic_meters = abs(max_x - min_x + 3) * abs(max_y - min_y + 3) - len(seen)
    print("Part1: how many cubic meters of lava could it hold? " + str(cubic_meters))


if __name__ == "__main__":
    main()
