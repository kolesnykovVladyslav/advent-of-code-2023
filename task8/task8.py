import re


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        # Task 1
        _map = {}
        instructions = lines[0]

        for line in lines[2:]:
            row = list(re.findall('[A-Z]{3}', line))
            _map[row[0]] = (row[1], row[2])

        solve_a(_map, instructions)
        solve_b(_map, instructions)


def solve_b(_map, instructions):
    positions = [position for position in _map.keys() if position.endswith("A")]
    step = 0
    while True:
        index = step % (len(instructions) - 1)
        step += 1
        instruction = instructions[index]

        all_z_positions = True
        for i in range(len(positions)):
            position = positions[i]
            node = _map[position]
            if instruction == "L":
                positions[i] = node[0]
            if instruction == "R":
                positions[i] = node[1]
            all_z_positions &= positions[i].endswith("Z")

        if all_z_positions:
            break

    print("Task 2: How many steps does it take before you're only on nodes that end with Z" + str(step))


# returns number of steps to go from AAA to ZZZ position
def solve_a(_map, instructions):
    position = "AAA"
    step = 0
    while True:
        index = step % (len(instructions) - 1)
        instruction = instructions[index]
        node = _map[position]
        if instruction == "L":
            position = node[0]
        if instruction == "R":
            position = node[1]
        step += 1
        if position == "ZZZ":
            break
    print("Task 1: How many steps are required to reach ZZZ? " + str(step))


if __name__ == "__main__":
    main()
