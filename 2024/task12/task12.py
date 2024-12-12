import time


class Cell:
    def __init__(self, char, visited=False):
        self.char = char
        self.visited = visited


def get_input(lines):
    grid = list()
    for line in lines:
        row = list()
        for char in line:
            if char == "\n":
                continue
            row.append(Cell(char, False))
        grid.append(row)
    return grid


def is_position_in(grid, position):
    return 0 <= position[0] < len(grid) and 0 <= position[1] < len(grid[0])


def solve(grid):
    price = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if not cell.visited:
                price += get_price_for_region(grid, (i, j))
    print("Total price = " + str(price))


def get_price_for_region(grid, initial_pos):
    queue = [initial_pos]
    area = 0
    perimeter = 0
    while len(queue) > 0:
        pos = queue.pop()
        cell = grid[pos[0]][pos[1]]
        cell.visited = True
        area += 1
        concurrent_perimeter = 4
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_pos = (pos[0] + dx, pos[1] + dy)
            if not is_position_in(grid, new_pos):
                continue
            next_cell = grid[new_pos[0]][new_pos[1]]
            if next_cell.char != cell.char:
                continue
            concurrent_perimeter -= 1
            if next_cell.visited:
                continue
            next_cell.visited = True
            queue.append(new_pos)
        perimeter += concurrent_perimeter
    return area * perimeter


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        grid = get_input(lines)
        solve(grid)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
