import re


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        # task 1
        compute_sum_of_mul(lines)

        # task 2
        compute_sum_of_mul_with_instructions(lines)


def compute_sum_of_mul(lines):
    result = 0
    for line in lines:
        mult_groups = re.findall(r'mul\((\d+),(\d+)\)', line)
        result += sum([int(x) * int(y) for (x, y) in mult_groups])
    print("Sum of multiplications = " + str(result))


def compute_sum_of_mul_with_instructions(lines):
    result = 0
    enabled = True
    for line in lines:
        mult_groups = re.finditer(r'mul\((\d+),(\d+)\)|don\'t\(\)|do\(\)', line)
        for match_obj in mult_groups:
            match = match_obj.group(0)
            if match == "do()":
                enabled = True
                continue
            if match == "don't()":
                enabled = False
                continue
            if enabled:
                x, y = match_obj.groups()
                result += int(x) * int(y)
    print("Sum of multiplications with instructions= " + str(result))


if __name__ == "__main__":
    main()
