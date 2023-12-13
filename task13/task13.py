def main():
    with open("input.txt") as f:
        lines = [l for l in f.read().splitlines()]

        solve_a(lines)


def solve_a(lines):
    valley = []
    sum = 0
    for line in lines:
        if len(line) > 0:
            valley.append(line)
        else:
            sum += summarize_pattern(valley)
            valley.clear()
    print("What number do you get after summarizing all of your notes? " + str(sum))


def summarize_pattern(valley):
    # horizontal reflection scan
    sum = 100 * get_rows_number(valley)

    # vertical reflection scan
    transponed_valley = ["" for _ in range(len(valley[0]))]
    for row in valley:
        for j, char in enumerate(row):
            transponed_valley[j] += char

    sum += get_rows_number(transponed_valley)

    return sum


def get_rows_number(_valley):
    for i, line1 in enumerate(_valley[:-1]):
        if line1 == _valley[i + 1]:
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
