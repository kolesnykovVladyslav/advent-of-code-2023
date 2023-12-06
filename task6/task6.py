def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

        # Task 1
        time_list = list(map(int, lines[0].split()[1:]))
        distances = list(map(int, lines[1].split()[1:]))

        product = 1
        for time, distance in zip(time_list, distances):
            product *= find_num_ways_to_beat_record(time, distance)

        print("Task 1: product=" + str(product))


def find_num_ways_to_beat_record(total_time, distance):
    ways_to_win = 0
    for hold_millis in range(total_time):
        speed = hold_millis
        if distance < speed * (total_time - hold_millis):
            ways_to_win += 1
    return ways_to_win


if __name__ == "__main__":
    main()
