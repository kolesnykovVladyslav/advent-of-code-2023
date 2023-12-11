import re

galaxy_symbol = "#"
empty_symbol = "."


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        solve(lines, 2)
        solve(lines, 1000000)


def solve(space_map, multiplier):
    space_width = len(space_map[0]) - 1
    columns_with_no_galaxies = [True for _ in range(space_width)]
    rows_with_no_galaxies = set()

    # detect empty rows / columns
    for i, line in enumerate(space_map):

        if galaxy_symbol not in line:
            rows_with_no_galaxies.add(i)

        for j in range(space_width):
            columns_with_no_galaxies[j] &= line[j] != galaxy_symbol

    columns_with_no_galaxies = {i for i, has_no_galaxy in enumerate(columns_with_no_galaxies) if has_no_galaxy}

    # find galaxies
    galaxies_coordinates = get_galaxies_coordinates(space_map)

    # update coordinates
    multiplier -= 1
    for ind, coordinate in enumerate(galaxies_coordinates):
        x = coordinate[0]
        x += multiplier * len([i for i in rows_with_no_galaxies if i < x])
        y = coordinate[1]
        y += multiplier * len([j for j in columns_with_no_galaxies if j < y])
        galaxies_coordinates[ind] = (x, y)

    sum = get_sum_of_distances(galaxies_coordinates)
    print("What is the sum of these lengths? " + str(sum))


def get_galaxies_coordinates(space_map):
    galaxies_coordinates = []
    for i, row in enumerate(space_map):
        for match in re.finditer(galaxy_symbol, row):
            j = match.start()
            coordinate = (i, j)
            galaxies_coordinates.append(coordinate)

    return galaxies_coordinates


def get_sum_of_distances(galaxies_coordinates):
    sum = 0
    for i, coordinate1 in enumerate(galaxies_coordinates):
        for j in range(i + 1, len(galaxies_coordinates)):
            coordinate2 = galaxies_coordinates[j]
            distance = abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])
            sum += distance
    return sum


if __name__ == "__main__":
    main()
