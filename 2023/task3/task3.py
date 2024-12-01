import re

all_matches = []
matches_symbols = set()


def main():
    file = open('input.txt', 'r')
    _sum = 0

    line_count = 0
    while True:
        line = file.readline()
        if not line:
            break

        # extract symbols
        matches_symbols.update([(line_count, match.start()) for match in re.finditer(r'[^.\d\n]', line)])

        # extract all numbers
        for match in re.finditer(r'\d+', line):
            all_matches.append((line_count, match))

        line_count += 1

    for found_number in all_matches:
        if has_adjacent_symbol(found_number):
            num = int(found_number[1].group())
            _sum += num

    print("Sum of the part numbers in the engine schematic = " + str(_sum))
    file.close()


def has_adjacent_symbol(number):
    current_line = number[0]
    range_num = number[1].span()
    for i in range(current_line - 1, current_line + 2):
        for j in range(range_num[0] - 1, range_num[1] + 1):
            if (i, j) in matches_symbols:
                return True

    return False


if __name__ == "__main__":
    main()
