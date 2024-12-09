#!/usr/bin/env python

import argparse
import datetime
import os
import sys

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

DAY_TEMPLATE = """#!/usr/bin/env python

from utils import read_input_lines


def sum_lengths(lines):
    return sum([len(line) for line in lines])


if __name__ == "__main__":
    lines = read_input_lines()

    # TODO
    sum_lengths(lines)
"""

TEST_TEMPLATE = """import pytest

from {day_name} import sum_lengths


@pytest.mark.parametrize(
    "input,expected",
    [
        [["abc", "def"], 6],
    ],
)
def test_sum_lengths(input, expected):
    assert sum_lengths(input) == expected

"""


if __name__ == "__main__":
    today = datetime.date.today()

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-y",
        "--year",
        type=int,
        default=today.year,
        help="The year to create for",
    )

    parser.add_argument(
        "-d",
        "--day",
        type=int,
        help="The day to create for",
    )

    args = parser.parse_args()

    if not args.day:
        print("No day specified.")
        parser.print_usage()
        sys.exit(1)

    year_str = str(args.year)
    day_str = "{:02d}".format(args.day)
    day_name = f"day{day_str}"

    day_dir = os.path.join(
        ROOT_DIR,
        year_str,
        day_name,
    )

    # create the year directory
    os.makedirs(day_dir, exist_ok=True)

    # create the day file
    file_path = os.path.join(day_dir, day_name + ".py")
    with open(file_path, "w") as day_file:
        day_file.write(
            DAY_TEMPLATE.format(
                year=year_str,
                day=day_str,
                day_name=day_name,
            )
        )

    os.chmod(file_path, 0o744)

    # create the test file
    with open(os.path.join(day_dir, "test_" + day_name + ".py"), "w") as test_file:
        test_file.write(
            TEST_TEMPLATE.format(
                year=year_str,
                day=day_str,
                day_name=day_name,
            )
        )

    # create the input file
    with open(os.path.join(day_dir, "input.txt"), "w") as input_file:
        input_file.write("")

    # symlink the utils file
    os.symlink(os.path.join(ROOT_DIR, "utils.py"), os.path.join(day_dir, "utils.py"))
