def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        sum = 0
        for line in lines:
            sum += solve_a(line)
        print("Task 1: What is the sum of these extrapolated values? " + str(sum))


def solve_a(line):
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

    for i in range(len(histories) - 2, -1, -1):
        value1 = histories[i][-1]
        value2 = histories[i + 1][-1]
        histories[i].append(value2 + value1)

    return histories[0][-1]


if __name__ == "__main__":
    main()
