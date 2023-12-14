import re
from functools import cache

direction = 0


def main():
    with open("input.txt") as f:
        lines = [l for l in f.read().splitlines()]
        solve_b(lines)


def solve_a(grid):
    t_grid = rotate_left(tuple(grid))
    sum = count_load(t_grid)
    print("what is the total load on the north support beams? " + str(int(sum)))


def solve_b(grid):
    # 152173
    cycles = 1000000000
    steps = 1 + cycles * 4
    t_grid = grid
    for i in range(steps):
        t_grid = rotate_left(tuple(t_grid))
    sum = count_load(t_grid)
    print("what is the total load on the north support beams? " + str(int(sum)))


@cache
def rotate_left(grid):
    global direction
    grid = zip(*grid)
    new_grid = []
    for i, column in enumerate(grid):
        new_grid.append(shift_left(column))
    direction += 1
    return new_grid


def shift_left(column):
    column = "".join(list(column))
    matches = re.finditer(r"[^#]+", column)
    new_column = column
    for match in matches:
        n = match.group().count("O")
        first_index = match.start()
        last_index = match.end()

        insert_str = "".join("O" * n) + "".join("." * (len(match.group()) - n))
        if (direction % 4) > 1:
            insert_str = insert_str[::-1]
        new_column = new_column[:first_index] + insert_str + new_column[last_index:]

    return new_column


def count_load(grid):
    sum = 0
    for column in grid:
        length = len(column)
        for i, char in enumerate(column):
            if char == "O":
                sum += length - i

    return sum


if __name__ == "__main__":
    main()
