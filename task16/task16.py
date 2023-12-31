import enum


class Direction(enum.Enum):
    left = 0
    up = 1
    right = 2
    down = 3


class Beam:
    def __init__(self, coordinate, direction: Direction):
        self.coordinate = coordinate
        self.direction = direction


class Node:
    def __init__(self, char, visited=False, visited_directions=None):
        if visited_directions is None:
            visited_directions = set()
        self.char = char
        self.visited = visited
        self.visited_directions = visited_directions

    def is_visited_direction(self, direction: Direction):
        return direction in self.visited_directions


def main():
    with open("input.txt") as f:
        lines = [l for l in f.read().splitlines()]
        solve_a(lines)
        solve_b(lines)


def get_grid(lines):
    grid = []
    for line in lines:
        grid_line = [Node(char, False) for char in line]
        grid.append(grid_line)
    return grid


def solve_b(lines):
    beams = []
    grid = get_grid(lines)
    for y in range(len(grid)):
        beams.append(Beam((0, y), Direction.right))
        beams.append(Beam((len(grid) - 1, y), Direction.left))

    for x in range(len(grid[0])):
        beams.append(Beam((x, len(grid) - 1), Direction.up))
        beams.append(Beam((x, 0), Direction.down))

    energized_counter = max([calculate_energized_cells(get_grid(lines), beam) for beam in beams])
    print("Part2: How many tiles end up being energized? " + str(energized_counter))


def solve_a(lines):
    grid = get_grid(lines)
    beam = Beam((0, 0), Direction.right)
    energized_counter = calculate_energized_cells(grid, beam)
    print("Part1: How many tiles end up being energized? " + str(energized_counter))


def calculate_energized_cells(grid, beam):
    width = len(grid[0])
    height = len(grid)
    beams = [beam]
    energized_counter = 0

    while len(beams) > 0:
        for beam in beams:
            x = beam.coordinate[0]
            y = beam.coordinate[1]

            # remove beam if outside
            if (x < 0 or width - 1 < x or y < 0 or height - 1 < y) and beam in beams:
                beams.remove(beam)
                continue

            node = grid[y][x]

            if not node.visited:
                node.visited = True
                energized_counter += 1

            if not node.is_visited_direction(beam.direction):
                node.visited_directions.update({beam.direction})
            else:
                beams.remove(beam)

            # check char
            if node.char == "|":
                if beam.direction in (Direction.right, Direction.left):
                    beam.direction = Direction.down
                    beams.append(Beam((x, y - 1), Direction.up))
            elif node.char == "-":
                if beam.direction in (Direction.up, Direction.down):
                    beam.direction = Direction.left
                    beams.append(Beam((x + 1, y), Direction.right))
            elif node.char == "/":
                if beam.direction == Direction.right:
                    beam.direction = Direction.up
                elif beam.direction == Direction.up:
                    beam.direction = Direction.right
                elif beam.direction == Direction.left:
                    beam.direction = Direction.down
                elif beam.direction == Direction.down:
                    beam.direction = Direction.left
            elif node.char == "\\":
                if beam.direction == Direction.right:
                    beam.direction = Direction.down
                elif beam.direction == Direction.down:
                    beam.direction = Direction.right
                elif beam.direction == Direction.left:
                    beam.direction = Direction.up
                elif beam.direction == Direction.up:
                    beam.direction = Direction.left

            # move
            new_x = beam.coordinate[0] + (1 if beam.direction == Direction.right else 0)
            new_x -= 1 if beam.direction == Direction.left else 0
            new_y = beam.coordinate[1] + (1 if beam.direction == Direction.down else 0)
            new_y -= 1 if beam.direction == Direction.up else 0
            beam.coordinate = (new_x, new_y)
    return energized_counter


if __name__ == "__main__":
    main()
