import re


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        # task 1
        compute_sum_of_mul(lines)


def compute_sum_of_mul(lines):
    result = 0
    for line in lines:
        mult_groups = re.findall(r'mul\((\d+),(\d+)\)', line)
        result += sum([int(x) * int(y) for (x, y) in mult_groups])
    print("Sum of multiplications = " + str(result))


if __name__ == "__main__":
    main()
