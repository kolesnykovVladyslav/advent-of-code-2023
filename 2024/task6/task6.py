import enum


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


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        grid, position = get_grid_and_start_position(lines)

        # task 1
        count_distinct_positions(grid, position)
        # task 2


if __name__ == "__main__":
    main()
