import copy
import enum


class Direction(enum.Enum):
    left = 0
    up = 1
    right = 2
    down = 3


class Crucible:
    def __init__(self, coordinate, direction: Direction = None):
        self.coordinate = coordinate
        self.direction = direction
        self.steps_forward = 0
        self.path_length = 0

    def turn_right_and_move(self):
        self.steps_forward = 1
        if self.direction == Direction.right:
            self.direction = Direction.down
            self.coordinate = (self.coordinate[0], self.coordinate[1] + 1)
        elif self.direction == Direction.down:
            self.direction = Direction.left
            self.coordinate = (self.coordinate[0] - 1, self.coordinate[1])
        elif self.direction == Direction.left:
            self.direction = Direction.up
            self.coordinate = (self.coordinate[0], self.coordinate[1] - 1)
        elif self.direction == Direction.up:
            self.direction = Direction.right
            self.coordinate = (self.coordinate[0] + 1, self.coordinate[1])

    def turn_left_and_move(self):
        self.steps_forward = 1
        if self.direction == Direction.down:
            self.direction = Direction.right
            self.coordinate = (self.coordinate[0] + 1, self.coordinate[1])
        elif self.direction == Direction.right:
            self.direction = Direction.up
            self.coordinate = (self.coordinate[0], self.coordinate[1] - 1)
        elif self.direction == Direction.up:
            self.direction = Direction.left
            self.coordinate = (self.coordinate[0] - 1, self.coordinate[1])
        elif self.direction == Direction.left:
            self.direction = Direction.down
            self.coordinate = (self.coordinate[0], self.coordinate[1] + 1)

    def move_forward(self):
        self.steps_forward += 1
        if self.steps_forward > 3:
            return

        if self.direction == Direction.down:
            self.coordinate = (self.coordinate[0], self.coordinate[1] + 1)
        elif self.direction == Direction.right:
            self.coordinate = (self.coordinate[0] + 1, self.coordinate[1])
        elif self.direction == Direction.up:
            self.coordinate = (self.coordinate[0], self.coordinate[1] - 1)
        elif self.direction == Direction.left:
            self.coordinate = (self.coordinate[0] - 1, self.coordinate[1])


class Node:
    def __init__(self, heat_loss: int):
        self.heat_loss = heat_loss
        self.min_heat_loss_path = None


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

    crucible = Crucible((0, 0), Direction.right)
    queue = [crucible]

    while len(queue) > 0:
        crucible = queue.pop()
        x, y = crucible.coordinate
        if x < 0 or width - 1 < x or y < 0 or height - 1 < y:
            continue

        current_node = grid[y][x]
        crucible.path_length += current_node.heat_loss

        if grid[height - 1][width - 1].min_heat_loss_path is not None and grid[height - 1][
            width - 1].min_heat_loss_path <= crucible.path_length + (width - x) + (height - y):
            continue

        if current_node.min_heat_loss_path is not None and current_node.min_heat_loss_path <= crucible.path_length:
            continue

        current_node.min_heat_loss_path = crucible.path_length
        # move
        crucible_left = copy.copy(crucible)
        crucible_left.turn_left_and_move()
        crucible_right = copy.copy(crucible)
        crucible_right.turn_right_and_move()
        crucible_forward = copy.copy(crucible)
        crucible_forward.move_forward()
        queue.append(crucible_left)
        queue.append(crucible_right)
        queue.append(crucible_forward)

    min_heat_loss_path = grid[height - 1][width - 1].min_heat_loss_path - grid[0][0].heat_loss
    print("Part1: What is the least heat loss it can incur? " + str(min_heat_loss_path))


def main():
    with open("input.txt") as f:
        lines = [l for l in f.read().splitlines()]
        solve_a(lines)


if __name__ == "__main__":
    main()
