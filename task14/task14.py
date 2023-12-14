import re


def get_columns(lines):
    columns = ["" for _ in range(len(lines[0]))]
    for line in lines:
        for j, char in enumerate(line):
            columns[j] += char

    return columns


def main():
    with open("input.txt") as f:
        lines = [l for l in f.read().splitlines()]
        grid = get_columns(lines)
        solve_a(grid)


def solve_a(grid):
    sum = get_north_load(grid)
    print("what is the total load on the north support beams? " + str(int(sum)))


def get_north_load(grid):
    sum = 0
    for column in grid:
        matches = re.finditer(r"[^#]+", column)
        for match in matches:
            n = match.group().count("O")
            first_index = match.start()
            distance = len(column) - first_index
            group_sum = (distance + (distance - n + 1)) * n / 2
            sum += group_sum
    return sum


if __name__ == "__main__":
    main()
