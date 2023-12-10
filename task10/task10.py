class Node:
    def __init__(self, pipe: str, is_outer=False):
        self.pipe = pipe
        self.distance = -1
        self.is_outer = is_outer

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

        all_cells = len(grid) * len(grid[0])
        cells_in_loop = 0
        for row in grid:
            for node in row:
                if node.is_visited():
                    cells_in_loop += 1

        outer_cells = 0
        start = (0, 0)
        queue = []
        queue.append(start)
        while len(queue) > 0:
            position = queue.pop(0)
            row = position[0]
            column = position[1]
            node = grid[row][column]
            if not node.is_visited():
                outer_cells += 1
                node.is_outer = True
                node.distance = 9999
                queue.append((row - 1, column))
                queue.append((row + 1, column))
                queue.append((row, column - 1))
                queue.append((row, column + 1))

        enclosed_count = all_cells - cells_in_loop - outer_cells

        print("How many tiles are enclosed by the loop? " + str(enclosed_count))

        for row in grid:
            for node in row:
                value = 1 if node.is_visited() else 8
                value = 0 if node.is_outer else value
                print(value, end="")
            print()


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
