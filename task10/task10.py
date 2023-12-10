class Node:
    def __init__(self, pipe: str):
        self.pipe = pipe
        self.distance = -1

    def is_visited(self):
        return self.distance >= 0


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        # build grid
        grid = []
        start = None
        for i, line in enumerate(lines):
            grid_line = []
            for j, pipe in enumerate(line):
                node = Node(pipe)
                grid_line.append(node)
                if pipe == "S":
                    start = (i, j)
            grid.append(grid_line)

        # start traverse through grid
        max_dist = 0
        queue = []
        # grid[start[0]][start[1]].distance = 0
        # queue.append(start)
        queue.append((start[0] - 1, start[1]))
        queue.append((start[0] + 1, start[1]))
        grid[start[0] - 1][start[1]].distance = 1
        grid[start[0] + 1][start[1]].distance = 1

        while len(queue) > 0:
            position = queue.pop(0)
            current_node: Node = grid[position[0]][position[1]]
            neighbour_nodes = get_neighbours(grid, position)
            max_dist = max(max_dist, current_node.distance)

            for neighbour_node in neighbour_nodes:
                node = grid[neighbour_node[0]][neighbour_node[1]]
                if node.distance > current_node.distance + 1 or node.distance == -1:
                    node.distance = current_node.distance + 1
                    queue.append(neighbour_node)

        print(
            "How many steps along the loop does it take to get from the starting position to the point farthest "
            "from the starting position? " + str(max_dist))

        enclosed_count = 0
        for i, row in enumerate(grid):
            for j, node in enumerate(row):
                if not node.is_visited():
                    is_enclosed_left = False
                    is_enclosed_right = False
                    is_enclosed_above = False
                    is_enclosed_below = False
                    for i_neighbour in range(0, i):
                        if grid[i_neighbour][j].is_visited():
                            is_enclosed_left = True
                            break
                    for i_neighbour in range(i + 1, len(grid) - 1):
                        if grid[i_neighbour][j].is_visited():
                            is_enclosed_right = True
                            break
                    for j_neighbour in range(0, j):
                        if grid[i][j_neighbour].is_visited():
                            is_enclosed_above = True
                            break
                    for j_neighbour in range(j + 1, len(row)):
                        if grid[i][j_neighbour].is_visited():
                            is_enclosed_below = True
                            break

                    if is_enclosed_left and is_enclosed_right and is_enclosed_above and is_enclosed_below:
                        enclosed_count += 1

        print("How many tiles are enclosed by the loop? " + str(enclosed_count))


def get_neighbours(grid, position):
    row = position[0]
    column = position[1]
    current_node: Node = grid[row][column]
    pipe = current_node.pipe

    neighbours = []
    if pipe == "S":
        neighbours = []
    elif pipe == "|":
        neighbours = [(row - 1, column), (row + 1, column)]
    elif pipe == "-":
        neighbours = [(row, column - 1), (row, column + 1)]
    elif pipe == "L":
        neighbours = [(row - 1, column), (row, column + 1)]
    elif pipe == "J":
        neighbours = [(row - 1, column), (row, column - 1)]
    elif pipe == "7":
        neighbours = [(row, column - 1), (row + 1, column)]
    elif pipe == "F":
        neighbours = [(row, column + 1), (row + 1, column)]

    return neighbours


def is_valid_neighbour(grid, neighbour_position):
    row = neighbour_position[0]
    column = neighbour_position[1]
    node = grid[row][column]
    if node.pipe == ".":
        return False
    return True


if __name__ == "__main__":
    main()
