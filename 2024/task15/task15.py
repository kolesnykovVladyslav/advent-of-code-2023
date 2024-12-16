import time

part_two = True
walls = set()
boxes = set()
to_remove = set()
to_add = set()


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
    global _width
    _width = len(lines[0]) - 1
    if part_two:
        _width *= 2
    initial_pos = None
    instructions = ""
    for y, line in enumerate(lines):
        if line.startswith(("<", "v", "^", ">")):
            instructions += line.rstrip()
            continue
        global _height
        _height = y
        for x, char in enumerate(line):
            if part_two:
                x *= 2
            if char == "\n":
                continue
            if char == "@":
                initial_pos = (x, y)
            if char == "#":
                walls.add((x, y))
                if part_two:
                    walls.add((x + 1, y))
            if char == "O":
                boxes.add((x, y))
    return instructions, initial_pos


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
                line += "[]" if part_two else "0"
            elif not part_two:
                line += "."
            elif (x - 1, y) not in boxes:
                line += "."
        print(line)
    print()


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


def can_move_part2(x, y, instruction) -> bool:
    dx, dy = get_direction(instruction)
    pos = (x + dx, y + dy)
    if pos in walls:
        return False
    if pos in boxes or (pos[0] - 1, pos[1]) in boxes:
        if (pos[0] - 1, pos[1]) in boxes:
            pos = (pos[0] - 1, pos[1])
        next_x, next_y = pos
        if instruction == ">":
            next_x += 1
        movable = can_move_part2(next_x, next_y, instruction)
        if instruction in ["v", "^"]:
            movable &= can_move_part2(next_x + 1, next_y, instruction)
        if movable:
            to_add.add((pos[0] + dx, pos[1] + dy))
            to_remove.add(pos)
        return movable

    return True


def solve1(lines):
    global to_remove, to_add
    instructions, initial_pos = get_input(lines)

    x, y = initial_pos
    print("Step: " + str(0))
    print_map((x, y))

    for step, instruction in enumerate(instructions, start=1):

        dx, dy = get_direction(instruction)
        next_x = x + dx
        next_y = y + dy

        if part_two:
            if can_move_part2(x, y, instruction):
                x, y = next_x, next_y
                for pos in to_remove:
                    boxes.remove(pos)
                for pos in to_add:
                    boxes.add(pos)
            to_add.clear()
            to_remove.clear()
        else:
            if can_move(x, y, instruction):
                x, y = next_x, next_y

        print("Step: " + str(step) + " move:" + instruction)
        print_map((x, y))

    result = sum([get_distance(pos) for pos in boxes])
    print(result)


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        solve1(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
