import re
from enum import Enum


class Cubes(Enum):
    red = 12
    green = 13
    blue = 14


def main():
    file = open('games_input.txt', 'r')
    _sum = 0
    _power_sum = 0

    while True:
        line = file.readline()
        if not line:
            break

        _sum += get_game_id(line)
        _power_sum += get_power_of_cubes_set(line)

    print("Sum games IDs = " + str(_sum))
    print("Sum of the power of cube sets = " + str(_power_sum))
    file.close()


def get_game_id(line: str):
    dot_split = line.split(':')
    games = dot_split[1].split(';')

    for game in games:
        for cube in Cubes:
            cube_match = re.search(r'(\d+) ' + cube.name, game)
            cubs_num = cube_match.group(1) if cube_match else 0

            if int(cubs_num) > cube.value:
                # game is impossible
                return 0

    game_id = re.search(r'(\d+)', dot_split[0]).group()
    return int(game_id)


def get_power_of_cubes_set(line):
    dot_split = line.split(':')
    games = dot_split[1].split(';')
    fewest_cubes = {cube.name: 0 for cube in Cubes}

    for game in games:
        for cube in Cubes:
            cube_match = re.search(r'(\d+) ' + cube.name, game)
            cubs_num = int(cube_match.group(1)) if cube_match else 0

            fewest_cubes[cube.name] = max(fewest_cubes[cube.name], cubs_num)

    power = 1
    for cube in fewest_cubes.values():
        power *= cube
    return power


if __name__ == "__main__":
    main()
