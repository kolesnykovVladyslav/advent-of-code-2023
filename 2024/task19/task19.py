import time


def count_ways(input, patterns, max_length, cache={}):
    if input in cache:
        return cache[input]
    if input == "":
        return 1
    total_ways = 0
    for i in range(1, min(max_length, len(input)) + 1):
        part = input[:i]
        if part in patterns:
            total_ways += count_ways(input[i:], patterns, max_length, cache)
    cache[input] = total_ways
    return total_ways


def solve(lines):
    patterns = set(lines[0].strip().replace(" ", "").split(','))
    max_length = max([len(pattern) for pattern in patterns])
    counter = 0
    total_ways = 0
    for input in lines[2:]:
        ways = count_ways(input.strip(), patterns, max_length)
        counter += int(ways > 0)
        total_ways += ways
    print(counter)
    print(total_ways)


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        solve(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
