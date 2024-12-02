import numpy as np


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        reports = get_reports(lines)
        # task 1
        calculate_safe_reports(reports)
        # task 2
        calculate_safe_reports(reports, tolerate_count=1)


def calculate_safe_reports(reports: list, tolerate_count: int = 0):
    safe_reports_count = len([report for report in reports if is_safe_report(report, tolerate_count)])
    print("How many reports are safe? = " + str(safe_reports_count))


def is_safe_report(report, tolerate_count: int):
    sign = np.sign(report[0] - report[1])
    for i, first in enumerate(report, start=1):
        if i >= len(report):
            break

        second = report[i]
        diff = first - second
        if not is_safe_diff(diff, sign):
            if tolerate_count <= 0:
                return False

            if i == 2:
                # maybe the problem is first element
                new_report3 = remove_report(report, i - 2)
                is_safe = is_safe_report(new_report3, tolerate_count - 1)
                if is_safe:
                    return True

            new_report1 = remove_report(report, i)
            new_report2 = remove_report(report, i - 1)

            return is_safe_report(new_report1, tolerate_count - 1) or is_safe_report(new_report2, tolerate_count - 1)

    return True


def is_safe_diff(diff, sign):
    return 1 <= abs(diff) <= 3 and sign == np.sign(diff)


def remove_report(report, index):
    new_report = report.copy()
    new_report.pop(index)
    return new_report


def get_reports(lines: list) -> list:
    reports = []
    for line in lines:
        reports.append([int(x) for x in line.split()])

    return reports


if __name__ == "__main__":
    main()
