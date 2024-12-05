#!/usr/bin/env python

from utils import format_lines_as_numbers


def safe_report(report, decrease=False):
    print(f"evaluating report {*report,}")

    iter_report = iter(report)
    previous = next(iter_report)
    for element in iter_report:
        if abs(element - previous) > 3:
            return False
        elif decrease and element < previous:
            print(f"  {element} is less than {previous}")
            previous = element
        elif not decrease and element > previous:
            print(f"  {element} is greater than {previous}")
            previous = element
        else:
            return False

    return True


def can_be_made_safe(report):
    for index in range(len(report)):
        spliced = report[:index] + report[(index + 1) :]
        if safe_report(spliced) or safe_report(spliced, decrease=True):
            return True
    return False


def safe_reports(reports):
    # Get the lists that are increasing or decreasing
    safe_reports = [
        report
        for report in reports
        if safe_report(report)
        or safe_report(report, decrease=True)
        or can_be_made_safe(report)
    ]

    print(f"total safe reports: {len(safe_reports)}")


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        lines = fp.readlines()

    reports = format_lines_as_numbers(lines)

    safe_reports(reports)
