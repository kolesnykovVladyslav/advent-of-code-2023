import re
from enum import Enum


class Cubes(Enum):
    red = 12
    green = 13
    blue = 14


def main():
    file = open('games_input.txt', 'r')
    _sum = 0

    while True:
        line = file.readline()
        if not line:
            break

        _sum += get_game_id(line)

    print("Sum games IDs = " + str(_sum))
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


if __name__ == "__main__":
    main()
