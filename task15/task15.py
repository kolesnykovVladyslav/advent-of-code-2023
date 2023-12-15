import re
from collections import OrderedDict

direction = 0


def main():
    with open("input.txt") as f:
        line = [l for l in f.read().splitlines()][0]
        values = line.split(",")
        solve_b(values)
        solve_a(values)


def solve_b(values):
    _sum = 0
    boxes = dict()

    for _str in values:
        label = re.search(r"[a-z]*", _str).group()
        box_number = get_hash(label)
        if box_number not in boxes:
            boxes[box_number] = OrderedDict()

        if "-" in _str and label in boxes[box_number]:
            boxes[box_number].pop(label)
            if len(boxes[box_number]) == 0:
                boxes.pop(box_number)
        elif "=" in _str:
            focal_length = int(_str[-1])
            boxes[box_number][label] = focal_length

    for box_num in boxes:
        box = boxes[box_num]
        for slot, label in enumerate(box):
            _sum += (box_num + 1) * (slot + 1) * box[label]

    print("Part2: What is the sum of the results? " + str(int(_sum)))


def solve_a(values):
    _sum = sum([get_hash(_str) for _str in values])
    print("Part1: What is the sum of the results? " + str(int(_sum)))


def get_hash(_str):
    current_value = 0
    for char in _str:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256
    return current_value


if __name__ == "__main__":
    main()
