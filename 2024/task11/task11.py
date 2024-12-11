import time
from functools import cache


# cache = {}


def get_input(lines):
    return [int(x) for x in lines[0].split()]


@cache
def blink(stone, times):
    # if (stone, times) in cache:
    #    return cache[(stone, times)]
    stones = []
    if stone == 0:
        stones = [1]
    elif len(str(stone)) % 2 == 0:
        length = len(str(stone))
        stones = [int(str(stone)[:length // 2]), int(str(stone)[length // 2:])]
    else:
        stones = [stone * 2024]

    # cache[(stone, times)] = stones

    if times == 1:
        return stones
    else:
        result = []
        for sub_stone in stones:
            result += blink(sub_stone, times - 1)

        # cache[(stone, times)] = result
        return result


def solve(input, times):
    stones = []
    for stone in input:
        stones += blink(stone, times)
    print("Stones number: " + str(len(stones)))


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        input = get_input(lines)
        solve(input, 25)
        # solve(input, 50)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
