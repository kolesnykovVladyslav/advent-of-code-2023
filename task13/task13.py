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


def solve_a(grid):
    sum = 0
    for valley in grid:
        sum += summarize_pattern(valley)
    print("What number do you get after summarizing all of your notes? " + str(sum))


def summarize_pattern(valley):
    # horizontal reflection scan
    sum = 100 * find_reflection(valley)

    # vertical reflection scan
    transponed_valley = ["" for _ in range(len(valley[0]))]
    for row in valley:
        for j, char in enumerate(row):
            transponed_valley[j] += char

    sum += find_reflection(transponed_valley)

    return sum


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
