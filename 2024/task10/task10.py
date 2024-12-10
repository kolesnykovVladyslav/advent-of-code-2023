class Position:
    def __init__(self, coordinate, height, visited=False):
        self.coordinate = coordinate
        self.height = height
        self.visited = visited


def get_input(lines):
    map = list()
    trailheads = set()
    for i, line in enumerate(lines):
        row = []
        for j, char in enumerate(line):
            height = int(char if char.isdigit() else -1)
            row.append(height)
            if height == 0:
                trailheads.add((i, j))
        map.append(row)

    return map, trailheads


def solve(map, trailheads):
    map_width = len(map[0]) - 1
    map_height = len(map)
    score_part1 = 0
    score_part2 = 0
    for trailhead in trailheads:
        top_positions = list()
        positions = [Position(trailhead, 0, False)]
        while len(positions) > 0:
            position = positions.pop(0)

            if position.visited:
                continue
            position.visited = True
            for move in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                new_coordinate = (position.coordinate[0] + move[0], position.coordinate[1] + move[1])
                if 0 <= new_coordinate[0] < map_height and 0 <= new_coordinate[1] < map_width:
                    height = map[new_coordinate[0]][new_coordinate[1]]
                    if height == position.height + 1:
                        if height == 9:
                            top_positions.append((new_coordinate[0], new_coordinate[1]))
                        positions.append(Position(new_coordinate, height, False))
        score_part1 += len(set(top_positions))
        score_part2 += len(top_positions)

    # task 1
    print("part1: " + str(score_part1))
    # task 2
    print("part2: " + str(score_part2))


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        map, trailheads = get_input(lines)
        solve(map, trailheads)


if __name__ == "__main__":
    main()
