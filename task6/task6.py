import math


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        # Task 1
        time_list = list(map(int, lines[0].split()[1:]))
        distances = list(map(int, lines[1].split()[1:]))

        product = 1
        for time, distance in zip(time_list, distances):
            product *= get_ways_to_beat_record(time, distance)

        print("Task 1: product=" + str(product))

        time_list = list(map(int, lines[0].split()[1:]))
        distances = list(map(int, lines[1].split()[1:]))
        product2 = 1
        for time, distance in zip(time_list, distances):
            product2 *= get_ways_to_beat_record(time, distance)

        print("Task 2: product=" + str(product2))


def get_ways_to_beat_record(total_time, distance):
    upper_bound = math.floor((total_time + math.sqrt(total_time ** 2 - 4 * distance)) / 2)
    lower_bound = math.ceil((total_time - math.sqrt(total_time ** 2 - 4 * distance)) / 2)

    return upper_bound - lower_bound + 1


if __name__ == "__main__":
    main()
