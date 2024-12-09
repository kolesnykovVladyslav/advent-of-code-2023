class File:
    def __init__(self, id, blocks, free_space):
        self.id = int(id)
        self.blocks = int(blocks)
        self.free_space = int(free_space)


def get_input(line):
    files = []
    for i in range(0, len(line), 2):
        files.append(File(id=i / 2, blocks=line[i], free_space=(line[i + 1] if i + 1 < len(line) else 0)))
    return files


def print_files(files):
    output = ""
    for file in files:
        output += str(file.id) * file.blocks + '.' * file.free_space
    print(output)


def solve(files):
    file_system = []
    for i, file1 in enumerate(files):
        for _ in range(0, file1.blocks):
            file_system.append(file1.id)

        if file1.free_space > 0:
            for j in range(len(files) - 1, i, -1):
                file2 = files[j]
                while file2.blocks > 0 and file1.free_space > 0:
                    file2.free_space += 1
                    file2.blocks -= 1
                    file1.free_space -= 1
                    file_system.append(file2.id)
        for _ in range(0, file1.free_space):
            file_system.append(0)

    check_sum = 0
    for i, id in enumerate(file_system):
        check_sum += i * id
    print("checksum = " + str(check_sum))


def main():
    with open('input.txt', 'r') as file:
        line = file.readlines()[0]
        files = get_input(line)
        print_files(files)

        # task 1
        solve(files)

        # task 2


if __name__ == "__main__":
    main()
