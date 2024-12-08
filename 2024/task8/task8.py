import re
from collections import defaultdict

import numpy as np


def get_input(lines):
    antennas_positions = defaultdict(list)
    for i, line in enumerate(lines):
        matches = re.finditer(r'\w', line)
        for match in matches:
            elem = match.group()
            j = match.start()
            antennas_positions[elem].append((i, j))
    return antennas_positions


def print_map(lines, pos):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if (i, j) in pos:
                line = line[:j] + "#" + line[j + 1:]
        print(line)


def get_dist(pos1, pos2):
    return (abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))


def is_pos_in_map(pos, map_size) -> bool:
    return 0 <= pos[0] < map_size[0] and 0 <= pos[1] < map_size[1]


def solve(antennas_map, map_size, part_two=False):
    antinodes_positions = set()
    antennas_position = set([x for xs in antennas_map.values() for x in xs])
    for value, positions in antennas_map.items():
        for i, pos1 in enumerate(positions):
            for pos2 in positions[i + 1:]:
                dist = get_dist(pos1, pos2)

                antinode1 = pos1
                antinode2 = pos2

                while True:
                    added = False
                    antinode1 = (
                        antinode1[0] + int(np.sign(antinode1[0] - antinode2[0])) * dist[0],
                        antinode1[1] + int(np.sign(antinode1[1] - antinode2[1])) * dist[1])
                    antinode2 = (
                        antinode2[0] - int(np.sign(antinode1[0] - antinode2[0])) * dist[0],
                        antinode2[1] - int(np.sign(antinode1[1] - antinode2[1])) * dist[1])
                    if is_pos_in_map(antinode1, map_size):
                        antinodes_positions.add(antinode1)
                        added = True
                    if is_pos_in_map(antinode2, map_size):
                        antinodes_positions.add(antinode2)
                        added = True

                    if not part_two or not added:
                        break

    if part_two:
        antinodes_positions = antinodes_positions.union(antennas_position)
    print("Number of antinodes within map = " + str(len(antinodes_positions)))
    
    return antinodes_positions


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        antennas_positions = get_input(lines)
        map_size = (len(lines), len(lines[0]) - 1)
        # task 1
        pos = solve(antennas_positions, map_size, part_two=False)
        print_map(lines, pos)
        # task 2
        solve(antennas_positions, map_size, part_two=True)


if __name__ == "__main__":
    main()
