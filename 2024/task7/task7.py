def get_input(lines):
    inputs = []
    for line in lines:
        x, values = line.split(":")
        values = [int(n) for n in values.split()]
        inputs.append((int(x), values))
    return inputs


def can_be_true_with_concat(result_value, values, with_concat=False):
    first = values.pop(0)
    intermediate_values = [first]
    for value in values:
        intermediate_values_for_value = intermediate_values
        intermediate_values = []
        for x in intermediate_values_for_value:
            sum = x + value
            if sum <= result_value:
                intermediate_values.append(sum)
            mult = x * value
            if mult <= result_value:
                intermediate_values.append(mult)
            # concat
            if not with_concat:
                continue
            concat = int(str(x) + str(value))
            if concat <= result_value:
                intermediate_values.append(concat)

    return result_value in set(intermediate_values)


def solve1(inputs):
    result = 0
    for input in inputs:
        x = input[0]
        values = input[1].copy()
        if can_be_true_with_concat(x, values, False):
            result += x

    print("total calibration result = " + str(result))


def solve2(inputs):
    result = 0
    for input in inputs:
        x = input[0]
        values = input[1].copy()
        if can_be_true_with_concat(x, values, True):
            result += x

    print("total calibration result = " + str(result))


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        inputs = get_input(lines)
        # task 1
        solve1(inputs)
        # task 2
        solve2(inputs)


if __name__ == "__main__":
    main()
