import re
import time
from functools import cache

wires = {}
gates = {}


def parse_input(lines):
    for line in lines:
        wires_match = re.search(r"(\w+):\s(\d)", line)
        if wires_match:
            wires[wires_match.group(1)] = int(wires_match.group(2))
            continue
        gates_match = re.search(r"(\w+)\s(\w+)\s(\w+)\s->\s(\w+)", line)
        if gates_match:
            gates[gates_match.group(4)] = (gates_match.group(2), gates_match.group(1), gates_match.group(3))


@cache
def evaluate_expression(gate):
    expression = gates[gate]
    a = wires[expression[1]] if expression[1] in wires else evaluate_expression(expression[1])
    b = wires[expression[2]] if expression[2] in wires else evaluate_expression(expression[2])
    if expression[0] == "AND":
        return a & b
    elif expression[0] == "OR":
        return a | b
    elif expression[0] == "XOR":
        return a ^ b
    return None


def solve():
    gates_with_z = [gate for gate in gates if gate.startswith("z")]
    gates_with_z.sort(reverse=True)
    binary = "".join([str(evaluate_expression(gate)) for gate in gates_with_z])
    decimal = int(binary, 2)
    print(decimal)


if __name__ == "__main__":
    start_time = time.time()
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        parse_input(lines)
        solve()

    print("--- %s seconds ---" % (time.time() - start_time))
