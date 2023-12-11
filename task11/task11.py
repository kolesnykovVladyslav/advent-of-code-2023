import re

galaxy_symbol = "#"
empty_symbol = "."


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        solve_a(lines)


def solve_a(lines):
    space_map = build_space_map(lines)
    galaxies_coordinates = []

    # find galaxies
    for i, row in enumerate(space_map):
        for match in re.finditer(galaxy_symbol, row):
            j = match.start()
            coordinate = (i, j)
            galaxies_coordinates.append(coordinate)

    sum = 0
    for i, coordinate1 in enumerate(galaxies_coordinates):
        for j in range(i + 1, len(galaxies_coordinates)):
            coordinate2 = galaxies_coordinates[j]
            distance = abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])
            sum += distance

    print("What is the sum of these lengths? " + str(sum))


def build_space_map(lines):
    space_map = []
    # expend space
    space_width = len(lines[0]) - 1
    column_has_no_galaxy = [True for _ in range(space_width)]
    for line in lines:
        for i in range(space_width):
            column_has_no_galaxy[i] &= line[i] != galaxy_symbol

        space_map.append(line)
        if galaxy_symbol not in line:
            space_map.append(line)
    column_has_no_galaxy.reverse()
    for j, has_no_galaxy in enumerate(column_has_no_galaxy):
        index = space_width - j - 1
        if has_no_galaxy:
            for i in range(len(space_map)):
                row = space_map[i]
                space_map[i] = row[:index] + empty_symbol + row[index:]

    return space_map


if __name__ == "__main__":
    main()
