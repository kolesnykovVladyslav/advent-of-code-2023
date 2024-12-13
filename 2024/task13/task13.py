import re
import time

import numpy as np
from numpy import array
from sympy import solve, Matrix


def get_input(lines):
    pattern = r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)'
    i = 0
    inputs = []
    inp = ""
    for line in lines:
        if i < 3:
            inp += line
        if i == 3:
            inputs.append(inp)
            i = -1
            inp = ""
        i += 1

    arrays = []
    for input_str in inputs:
        match = re.search(pattern, input_str)
        if match:
            a_x = float(match.group(1))
            a_y = float(match.group(2))
            b_x = float(match.group(3))
            b_y = float(match.group(4))
            prize_x = float(match.group(5))
            prize_y = float(match.group(6))
            # simpy
            arrays.append(np.array([[a_x, b_x, prize_x], [a_y, b_y, prize_y]]))
            # numpy
            # arrays.append(np.array([[a_x, b_x], [a_y, b_y], [prize_x, prize_y]]))
        else:
            raise ValueError("Input string does not match the expected format")
    return arrays


def is_round(n):
    return n % 1 < 0.1


def solve(arrays):
    total_tokens = 0
    for arr in arrays:
        # a, b = solve_numpy(arr)
        a, b = solve_simpy(arr)

        if 0 <= a <= 100 and is_round(a) and 0 <= b <= 100 and is_round(b):
            total_tokens += 3 * round(a) + round(b)
    print("Total price = " + str(total_tokens))


def solve_numpy(arr):
    x = array(arr[:-1])
    y = array(arr[-1])
    return np.linalg.solve(x, y)


def solve_simpy(arr):
    # Define the augmented matrix
    augmented_matrix = Matrix(arr)
    # Solve the system
    reduced_row_echelon_form = augmented_matrix.rref()[0]
    solution = reduced_row_echelon_form[:, -1]
    return solution[0], solution[1]


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        arrays = get_input(lines)
        solve(arrays)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
