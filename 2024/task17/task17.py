import time


def get_input(lines):
    a = int(lines[0].split(': ')[1])
    b = int(lines[1].split(': ')[1])
    c = int(lines[2].split(': ')[1])
    program = list(map(int, lines[4].split(': ')[1].split(',')))
    return a, b, c, program


def get_combo_operand(operand, a, b, c):
    if operand in range(0, 4):
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:
        return None


def solve(lines):
    a, b, c, program = get_input(lines)
    output = []
    instruction_pointer = 0
    while instruction_pointer < len(program):
        instruction = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        combo_operand = get_combo_operand(operand, a, b, c)
        match instruction:
            case 0:
                denominator = 2 ** combo_operand
                a = a // denominator
            case 1:
                b = b ^ operand
            case 2:
                b = combo_operand % 8
            case 3:
                if a != 0:
                    instruction_pointer = operand
                    continue
            case 4:
                b = b ^ c
            case 5:
                output.append(combo_operand % 8)
            case 6:
                denominator = 2 ** combo_operand
                b = a // denominator
            case 7:
                denominator = 2 ** combo_operand
                c = a // denominator
        instruction_pointer += 2

    print(",".join([str(x) for x in output]))


if __name__ == "__main__":
    start_time = time.time()
    with open('test_input_part2.txt', 'r') as file:
        lines = file.readlines()
        solve(lines)
    print("--- %s seconds ---" % (time.time() - start_time))
