import re

all_matches = []
matches_symbols = set()
star_neighbours = dict.fromkeys((), [])


def main():
    file = open('input.txt', 'r')
    _sum = 0

    line_count = 0
    while True:
        line = file.readline()
        if not line:
            break

        # extract symbols
        matches_symbols.update([(line_count, match.start()) for match in re.finditer(r'\*', line)])

        # extract all numbers
        for match in re.finditer(r'\d+', line):
            all_matches.append((line_count, match))

        line_count += 1

    for found_number in all_matches:
        detect_neighbours(found_number)

    for neighbours in star_neighbours.values():
        if len(neighbours) == 2:
            gear_ratio = neighbours[0] * neighbours[1]
            _sum += gear_ratio

    print("Sum of the part numbers in the engine schematic = " + str(_sum))
    file.close()


def detect_neighbours(number):
    current_line = number[0]
    range_num = number[1].span()
    num = int(number[1].group())
    for i in range(current_line - 1, current_line + 2):
        for j in range(range_num[0] - 1, range_num[1] + 1):
            if (i, j) in matches_symbols:
                if (i, j) not in star_neighbours:
                    star_neighbours[(i, j)] = []
                star_neighbours[(i, j)].append(num)


if __name__ == "__main__":
    main()
