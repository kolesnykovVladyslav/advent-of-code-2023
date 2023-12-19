import sys
from heapq import heappush, heappop

RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)


def get_left_right_neighbour(direction):
    if direction in [RIGHT, LEFT]:
        yield DOWN
        yield UP
    elif direction in [DOWN, UP]:
        yield RIGHT
        yield LEFT
    else:  # start
        yield RIGHT
        yield DOWN


def get_least_heat_loss(grid, _min, _max):
    final_position = (len(grid) - 1, len(grid[0]) - 1)
    heap = [(0, (0, 0), (0, 0))]
    dist_map = {(0, 0): 0}
    seen = set()
    cost = 0

    while heap:
        cost, position, direction = heappop(heap)
        if position == final_position:
            break
        if (position, direction) in seen:
            continue
        seen.add((position, direction))

        x, y = position
        for new_direction in get_left_right_neighbour(direction):
            neighbour_cost = cost
            dx, dy = new_direction
            for i in range(1, _max + 1):
                new_position = (x + i * dx, y + i * dy)
                if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= (len(grid)) or new_position[1] >= (
                        len(grid[0])):
                    continue
                neighbour_cost = neighbour_cost + int(grid[new_position[0]][new_position[1]])
                if i >= _min:
                    _pos = (new_position, (dx, dy))
                    if dist_map.get(_pos, sys.maxsize) <= neighbour_cost:
                        continue
                    dist_map[_pos] = neighbour_cost
                    heappush(heap, (neighbour_cost, new_position, new_direction))
    return cost


def main():
    with open("input.txt") as f:
        lines = [l for l in f.read().splitlines()]
        print("Part1: What is the least heat loss? " + str(get_least_heat_loss(lines, 0, 3)))


if __name__ == "__main__":
    main()
