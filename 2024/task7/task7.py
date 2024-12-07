def get_input(lines):
    inputs = []
    for line in lines:
        x, values = line.split(":")
        values = [int(n) for n in values.split()]
        inputs.append((int(x), values))
    return inputs


def can_be_true(result_value, values):
    intermediate_values = [result_value]
    for value in values:
        intermediate_values_for_value = intermediate_values
        intermediate_values = []
        for x in intermediate_values_for_value:
            diff = x - value
            if diff >= 0:
                intermediate_values.append(diff)
            if x % value == 0:
                div = x / value
                intermediate_values.append(div)

    return 0 in set(intermediate_values)


def solve1(inputs):
    result = 0
    for input in inputs:
        x = input[0]
        values = reversed(input[1])
        if can_be_true(x, values):
            result += x

    print("total calibration result = " + str(result))


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        inputs = get_input(lines)
        # task 1
        solve1(inputs)
        # task 2


if __name__ == "__main__":
    main()
