grid = []


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            grid.append(list(line))
        # task 1
        solve_part1()
        # task 2
        solve_part2()


def solve_part2():
    xmas_count = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            xmas_count += int(char == "A" and is_xmas(i, j))
    print("How many times does X-MAS appear? = " + str(xmas_count))


def is_xmas(i, j):
    diagonal1 = get_char_at_index(i - 1, j - 1) + get_char_at_index(i, j) + get_char_at_index(i + 1, j + 1)
    diagonal2 = get_char_at_index(i - 1, j + 1) + get_char_at_index(i, j) + get_char_at_index(i + 1, j - 1)
    return (diagonal1 == "MAS" or diagonal1 == "SAM") and (diagonal2 == "MAS" or diagonal2 == "SAM")


def solve_part1():
    xmas_count = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "X":
                # XMAS
                xmas_count += get_number_of_xmas_for_position(i, j, "MAS")
            if char == "S":
                # XMAS reverse => SAMX
                xmas_count += get_number_of_xmas_for_position(i, j, "AMX")
    print("How many times does XMAS appear? = " + str(xmas_count))


def get_number_of_xmas_for_position(i, j, word) -> int:
    up_right = True
    right = True
    low_right = True
    down = True
    for index, char in enumerate(word, 1):
        right &= get_char_at_index(i, j + index) == char
        up_right &= get_char_at_index(i - index, j + index) == char
        low_right &= get_char_at_index(i + index, j + index) == char
        down &= get_char_at_index(i + index, j) == char

    return sum(bool(x) for x in [up_right, right, low_right, down])


def get_char_at_index(i, j):
    if not (0 <= i < len(grid)):
        return ""
    row = grid[i]
    return row[j] if 0 <= j < len(row) else ""


if __name__ == "__main__":
    main()
