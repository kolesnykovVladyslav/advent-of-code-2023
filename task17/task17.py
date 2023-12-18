import heapq
import sys
from collections import defaultdict


class Node:
    def __init__(self, heat_loss: int):
        self.heat_loss = heat_loss
        self.visited = False
        self.dist = sys.maxsize
        self.dir_counter = defaultdict(lambda: 0, {})


def get_grid(lines):
    grid = []
    for line in lines:
        grid_line = [Node(int(value)) for value in line]
        grid.append(grid_line)
    return grid


def solve_a(lines):
    grid = get_grid(lines)
    height = len(grid)
    width = len(grid[0])

    grid[0][0].dist = 0
    queue = [(grid[0][0].dist, 0, 0)]

    while len(queue) > 0:
        _, x, y = heapq.heappop(queue)
        node = grid[y][x]
        if node.visited:
            continue
        node.visited = True
        # node.dir_counter.clear()

        # travers neighbours
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < width and 0 <= new_y < height:
                neighbour = grid[new_y][new_x]
                if node.dist + neighbour.heat_loss < neighbour.dist:

                    if node.dir_counter.get((dx, dy), 0) < 3:
                        neighbour.dir_counter = dict(node.dir_counter)
                        if (dx, dy) not in neighbour.dir_counter:
                            neighbour.dir_counter.clear()
                        neighbour.dir_counter[(dx, dy)] = neighbour.dir_counter.get((dx, dy), 0) + 1
                        neighbour.dist = node.dist + neighbour.heat_loss
                        heapq.heappush(queue, (neighbour.dist, new_x, new_y))

    min_heat_loss_path = grid[height - 1][width - 1].dist - grid[0][0].heat_loss
    print("Part1: What is the least heat loss it can incur? " + str(min_heat_loss_path))


def main():
    with open("input.txt") as f:
        lines = [l for l in f.read().splitlines()]
        solve_a(lines)


if __name__ == "__main__":
    main()
