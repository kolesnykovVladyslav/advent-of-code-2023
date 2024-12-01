def parse(lines):
    grids = [[]]
    for line in lines:
        if line == '':
            grids.append([])
            continue

        grids[-1].append(line)

    return grids


def main():
    with open("input.txt") as f:
        lines = [l for l in f.read().splitlines()]
        grid = parse(lines)
        solve_a(grid)
        solve_b(grid)


def solve_a(grid):
    sum = 0
    for valley in grid:
        sum += summarize_pattern(valley, find_reflection)
    print("What number do you get after summarizing all of your notes? " + str(sum))


def solve_b(grid):
    sum = 0
    for valley in grid:
        sum += summarize_pattern(valley, find_smudge)
    print("What number do you get after summarizing all of your notes? " + str(sum))


def summarize_pattern(valley, func):
    # horizontal reflection scan
    sum = 100 * func(valley)

    # vertical reflection scan
    transponed_valley = ["" for _ in range(len(valley[0]))]
    for row in valley:
        for j, char in enumerate(row):
            transponed_valley[j] += char

    sum += func(transponed_valley)

    return sum


def is_power_of_two(n):
    return (n & (n - 1) == 0) and n != 0


def convert_to_int(grid_line):
    grid_line = ''.join(grid_line).replace('.', '0').replace('#', '1')
    return int(grid_line, 2)


def find_smudge(_valley):
    encoded_grid = [convert_to_int(line) for line in _valley]

    for i in range(len(encoded_grid)):
        above = encoded_grid[i + 1:]
        below = encoded_grid[:i + 1]
        length = min(len(above), len(below))
        above = above[:length]
        below = list(reversed(below[-length:]))

        diff = [a ^ b for a, b in zip(above, below) if a != b]
        if len(diff) == 1 and is_power_of_two(diff[0]):
            return i + 1

    return 0


def find_reflection(_valley):
    for i, line in enumerate(_valley[:-1]):
        if line == _valley[i + 1]:
            # found equal lines nearby
            above = _valley[i + 1:]
            below = _valley[:i + 1]
            length = min(len(above), len(below))
            above = above[:length]
            below = list(reversed(below[-length:]))
            if above == below:
                return i + 1

    return 0


if __name__ == "__main__":
    main()
