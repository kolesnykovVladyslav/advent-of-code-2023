import time

cache = {}


def can_be_made(input, patterns, max_length):
    if input in cache:
        return cache[input]
    if input == "":
        return True
    for i in range(1, min(max_length, len(input)) + 1):
        part = input[:i]
        if part in patterns and can_be_made(input[i:], patterns, max_length):
            cache[input] = True
            return True
    cache[input] = False
    return False


def solve(lines):
    patterns = set(lines[0].strip().replace(" ", "").split(','))
    max_length = max([len(pattern) for pattern in patterns])
    counter = 0
    for input in lines[2:]:
        if can_be_made(input.strip(), patterns, max_length):
            counter += 1
    print(counter)


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        solve(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
