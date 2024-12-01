def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        compute_distance_of_two_lists(lines)


def compute_distance_of_two_lists(lines):
    first_list = []
    second_list = []
    for line in lines:
        first, second = line.split()
        first_list.append(first)
        second_list.append(second)

    first_list.sort()
    second_list.sort()

    distance = 0
    for first, second in zip(first_list, second_list):
        distance += abs(int(first) - int(second))

    print("Total distance between lists = " + str(distance))


if __name__ == "__main__":
    main()
