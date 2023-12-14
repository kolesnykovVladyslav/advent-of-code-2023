import re


def main():
    with open("input.txt") as f:
        lines = [l for l in f.read().splitlines()]
        solve_a(lines)


def solve_a(grid):
    t_grid = rotate_left(grid)
    sum = count_load(t_grid)
    print("what is the total load on the north support beams? " + str(int(sum)))


def rotate_left(grid):
    grid = zip(*grid)
    new_grid = []
    for i, column in enumerate(grid):
        new_grid.append(shift_left(column))
    return new_grid


def shift_left(column):
    column = "".join(list(column))
    matches = re.finditer(r"[^#]+", column)
    new_column = column
    for match in matches:
        n = match.group().count("O")
        first_index = match.start()
        last_index = match.end()
        new_column = new_column[:first_index] + "".join("O" * n) + "".join(
            "." * (len(match.group()) - n)) + new_column[last_index:]

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
