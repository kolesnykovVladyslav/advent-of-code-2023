import time


def parse_input(lines):
    heights = None
    keys, locks = [], []
    for row, line in enumerate(lines):
        line = line.strip()
        if row % 8 == 0:
            heights = [-1] * len(lines[0].strip())
            if set(line) == {"#"}:
                locks.append(heights)
            else:
                keys.append(heights)
        for col, char in enumerate(line):
            if char == '#':
                heights[col] += 1
    return keys, locks


def do_fit(key, lock) -> bool:
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False
    return True


def solve(lines):
    keys, locks = parse_input(lines)
    counter = 0
    for key in keys:
        for lock in locks:
            counter += int(do_fit(key, lock))
    print(counter)


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        solve(lines)

    print("--- %s seconds ---" % (time.time() - start_time))
