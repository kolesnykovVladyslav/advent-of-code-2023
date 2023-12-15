direction = 0


def main():
    with open("input.txt") as f:
        lines = [l for l in f.read().splitlines()]
        solve_a(lines[0])


def solve_a(line):
    values = line.split(",")
    _sum = sum([get_hash(_str) for _str in values])

    print("Part1: What is the sum of the results? " + str(int(_sum)))


def get_hash(_str):
    current_value = 0
    for char in _str:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value


if __name__ == "__main__":
    main()
