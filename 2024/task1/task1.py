from collections import Counter


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        first, second = get_two_lists(lines)

        # task 1
        compute_distance_of_two_lists(first, second)

        # task 2
        compute_similarity_score(first, second)


def get_two_lists(lines: list) -> (list, list):
    first_list, second_list = [], []
    for line in lines:
        first, second = line.split()
        first_list.append(int(first))
        second_list.append(int(second))

    return first_list, second_list


def compute_distance_of_two_lists(first_list: list, second_list: list):
    first_list.sort()
    second_list.sort()
    distance = 0
    for first, second in zip(first_list, second_list):
        distance += abs(first - second)

    print("Total distance between lists = " + str(distance))


def compute_similarity_score(first_list: list, second_list: list):
    second_list_counter = Counter(second_list)
    similarity_score = 0
    for x in first_list:
        similarity_score += x * (second_list_counter.get(x) or 0)

    print("Similarity score = " + str(similarity_score))


if __name__ == "__main__":
    main()
