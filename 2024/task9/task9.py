class File:
    def __init__(self, id, blocks, free_space, index=0):
        self.id = int(id)
        self.blocks = int(blocks)
        self.free_space = int(free_space)
        self.index = int(index)


def get_input(line):
    files = []
    index = 0
    for i in range(0, len(line), 2):
        files.append(File(id=i / 2, blocks=line[i], free_space=(line[i + 1] if i + 1 < len(line) else 0), index=index))
        index += int(line[i]) + int(line[i + 1] if i + 1 < len(line) else 0)
    return files


def print_files(files):
    output = ""
    for file in files:
        output += str(file.id) * file.blocks + '.' * file.free_space
    print(output)


def solveA(files):
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

    # print("".join([str(x) for x in file_system]))
    check_sum = sum(i * id for i, id in enumerate(file_system))
    print("checksum = " + str(check_sum))


def solveB(files):
    file_system = [0] * sum([file.blocks + file.free_space for file in files])
    new_files = files.copy()
    for i in range(len(files) - 1, 0, -1):
        file2 = files[i]

        for file1 in new_files:
            if file1.index >= file2.index or file1 == file2:
                continue
            if file1.free_space >= file2.blocks:
                file2.free_space = file1.free_space - file2.blocks
                file1.free_space = 0
                file2.index = file1.index + file1.blocks
                new_files.remove(file2)
                new_files.insert(new_files.index(file1) + 1, file2)
                break

    for file in new_files:
        for k in range(file.blocks):
            file_system[file.index + k] = file.id

    # print("".join([str(x) for x in file_system]))
    check_sum = sum(i * id for i, id in enumerate(file_system))
    print("checksum = " + str(check_sum))


def main():
    with open('input.txt', 'r') as file:
        line = file.readlines()[0]

        # task 1
        files = get_input(line)
        solveA(files)

        # task 2
        files = get_input(line)
        solveB(files)


if __name__ == "__main__":
    main()
