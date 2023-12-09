def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        histories = []
        for line in lines:
            histories.append(get_histories(line))

        print("Task 1: What is the sum of these extrapolated values? " + str(solve_a(histories)))
        print("Task 2: What is the sum of these extrapolated values? " + str(solve_b(histories)))


def solve_b(all_histories):
    sum = 0
    for histories in all_histories:
        for i in range(len(histories) - 2, -1, -1):
            value1 = histories[i][0]
            value2 = histories[i + 1][0]
            histories[i].insert(0, value1 - value2)
        sum += histories[0][0]
    return sum


def solve_a(all_histories):
    sum = 0
    for histories in all_histories:
        for i in range(len(histories) - 2, -1, -1):
            value1 = histories[i][-1]
            value2 = histories[i + 1][-1]
            histories[i].append(value2 + value1)
        sum += histories[0][-1]
    return sum


def get_histories(line):
    histories = []
    history = list(map(int, line.split()))
    while not (len(set(history)) == 1 and set(history).pop() == 0):
        diff_list = []
        for i in range(len(history) - 1):
            value1 = history[i]
            value2 = history[i + 1]
            diff_list.append(value2 - value1)
        histories.append(history)
        history = diff_list
    return histories


if __name__ == "__main__":
    main()
