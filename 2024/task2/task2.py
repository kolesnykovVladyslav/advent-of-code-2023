import numpy as np


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        reports = get_reports(lines)
        # task 1
        calculate_safe_reports(reports)
        # task 2


def calculate_safe_reports(reports: list):
    safe_reports_count = len([report for report in reports if is_safe_report(report)])
    print("How many reports are safe? = " + str(safe_reports_count))


def is_safe_report(report):
    sign = report[0] - report[1]
    for i, first in enumerate(report, start=1):
        if i >= len(report):
            break

        second = report[i]
        diff = first - second
        if not (1 <= abs(diff) <= 3 and np.sign(sign) == np.sign(diff)):
            return False
    return True


def get_reports(lines: list) -> list:
    reports = []
    for line in lines:
        reports.append([int(x) for x in line.split()])

    return reports


if __name__ == "__main__":
    main()
