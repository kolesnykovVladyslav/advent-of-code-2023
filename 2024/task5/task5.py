from collections import defaultdict


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        ordering_rules, page_numbers = get_input(lines)
        # task 1
        count_sum_of_middle_pages_for_correct_order(ordering_rules, page_numbers)


def count_sum_of_middle_pages_for_correct_order(ordering_rules, page_numbers):
    result = sum(page[len(page) // 2] for page in page_numbers if is_correct_order(ordering_rules, page))
    print("Sum of middle pages for correct order updates: ", result)


def is_correct_order(ordering_rules, page) -> bool:
    for i, x in enumerate(reversed(page), start=1):
        if x in ordering_rules:
            for j in range(len(page) - i - 1, -1, -1):
                y = page[j]
                if y in ordering_rules[x]:
                    return False
    return True


def get_input(lines):
    ordering_rules = defaultdict(set)
    page_numbers = []
    for line in lines:
        if "|" in line:
            x, y = line.split("|")
            ordering_rules[int(x)].add(int(y))
            continue
        page_numbers.append([int(x) for x in line.split(",")])
    return ordering_rules, page_numbers


if __name__ == "__main__":
    main()
