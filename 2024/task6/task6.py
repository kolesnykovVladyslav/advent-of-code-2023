import enum
from copy import deepcopy

obstacles = set()


class Direction(enum.Enum):
    left = (0, -1)
    up = (-1, 0)
    right = (0, 1)
    down = (1, 0)

    def turn_right(self):
        if self == Direction.left:
            return Direction.up
        elif self == Direction.up:
            return Direction.right
        elif self == Direction.right:
            return Direction.down
        elif self == Direction.down:
            return Direction.left


class Cell:
    def __init__(self, char):
        self.char = char
        self.visited = False

    def is_wall(self):
        return self.char == '#'


def get_grid_and_start_position(lines):
    start_position = None
    grid = []
    for i, line in enumerate(lines):
        row = []
        for j, char in enumerate(line):
            row.append(Cell(char))
            if char == '^':
                start_position = (i, j, Direction.up)
        grid.append(row)
    return grid, start_position


def is_position_in(grid, position):
    return 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])


def count_distinct_positions(grid, position):
    count = 0
    while is_position_in(grid, position):
        i, j, direction = position
        cell = grid[i][j]

        if cell.is_wall():
            # step back and turn right
            position = (i - direction.value[0], j - direction.value[1], direction.turn_right())
            continue

        if not cell.visited:
            cell.visited = True
            count += 1

        # move
        position = (i + direction.value[0], j + direction.value[1], direction)

    print("Number of distinct cells visited: ", count)


def solve_task2(grid, position):
    count = 0
    while is_position_in(grid, position):
        i, j, direction = position
        cell = grid[i][j]

        if cell.is_wall():
            # step back and turn right
            position = (i - direction.value[0], j - direction.value[1], direction.turn_right())
            continue

        # move
        next_i, next_j = i + direction.value[0], j + direction.value[1]
        position = (next_i, next_j, direction)

        if (next_i, next_j) not in obstacles and is_loop(grid, position):
            obstacles.add((next_i, next_j))
            count += 1

    print("Number of different positions for obstacle: ", count)


def is_loop(grid, position):
    new_grid = grid.copy()
    new_position = deepcopy(position)

    if not is_position_in(new_grid, new_position):
        return False
    initial_i, initial_j = new_position[0], new_position[1]
    old_char = grid[initial_i][initial_j].char
    new_grid[initial_i][initial_j].char = '#'

    cache = set()
    while is_position_in(grid, position):
        i, j, direction = position
        cell = grid[i][j]

        if cell.is_wall():
            # step back and turn right
            position = (i - direction.value[0], j - direction.value[1], direction.turn_right())
            continue

        if position in cache:
            # loop detected
            new_grid[initial_i][initial_j].char = old_char
            return True
        cache.add(position)

        # move
        position = (i + direction.value[0], j + direction.value[1], direction)

    new_grid[initial_i][initial_j].char = old_char
    return False


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        grid, position = get_grid_and_start_position(lines)

        # task 1
        count_distinct_positions(grid, position)
        # task 2
        solve_task2(grid, position)


if __name__ == "__main__":
    main()
