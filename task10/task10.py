class Node:
    def __init__(self, pipe: str):
        self.pipe = pipe
        self.distance = -1

    def is_visited(self):
        return self.distance >= 0


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

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
        print(grid[0][0].pipe)


if __name__ == "__main__":
    main()
