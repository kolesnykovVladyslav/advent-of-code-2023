import time

walls = set()
boxes = set()


def get_distance(pos):
    x, y = pos
    return abs(x) + 100 * abs(y)


def get_direction(char):
    if char == "<":
        return (-1, 0)
    elif char == "v":
        return (0, 1)
    elif char == "^":
        return (0, -1)
    elif char == ">":
        return (1, 0)
    else:
        return (0, 0)


def get_input(lines):
    initial_pos = None
    instructions = ""
    for y, line in enumerate(lines):
        if line.startswith(("<", "v", "^", ">")):
            instructions += line.rstrip()
            continue
        for x, char in enumerate(line):
            if char == "\n":
                continue
            global _width, _height
            _height = y + 1
            _width = len(line) - 1
            if char == "@":
                initial_pos = (x, y)
            if char == "#":
                walls.add((x, y))
            if char == "O":
                boxes.add((x, y))
    return instructions, initial_pos


def can_move(x, y, instruction, is_start=True) -> bool:
    dx, dy = get_direction(instruction)
    pos = (x + dx, y + dy)
    if pos in walls:
        return False
    if pos in boxes:
        next_x, next_y = pos
        movable = can_move(next_x, next_y, instruction, False)
        if movable and is_start:
            boxes.remove(pos)
        return movable

    if not is_start:
        boxes.add(pos)
    return True


def print_map(pos):
    global _width
    global _height

    for y in range(_height):
        line = ""
        for x in range(_width):
            if pos == (x, y):
                line += "@"
            elif (x, y) in walls:
                line += "#"
            elif (x, y) in boxes:
                line += "0"
            else:
                line += "."
        print(line)
    print()


def solve1(lines):
    instructions, initial_pos = get_input(lines)

    x, y = initial_pos
    for step, instruction in enumerate(instructions, start=1):

        dx, dy = get_direction(instruction)
        next_x = x + dx
        next_y = y + dy

        if can_move(x, y, instruction):
            x, y = next_x, next_y

        # print("Step: " + str(step))
        # print_map((x, y))

    result = sum([get_distance(pos) for pos in boxes])
    print(result)


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        solve1(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
