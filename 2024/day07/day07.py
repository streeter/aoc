#!/usr/bin/env python

import operator

from utils import read_input_lines, ints


def concatenate(first: int, second: int) -> int:
    return int(f"{first}{second}")


def solve_equation(
    target: int, accumulator: int, numbers: list[int], operations
) -> bool:
    """
    If the equation can be solved, return True, else False
    """
    if not numbers:
        return accumulator == target

    for op in operations:
        if solve_equation(target, op(accumulator, numbers[0]), numbers[1:], operations):
            return True

    return False


if __name__ == "__main__":
    lines = read_input_lines()

    total_1 = 0
    total_2 = 0

    for line in lines:
        target, accumulator, *numbers = ints(line)

        if solve_equation(target, accumulator, numbers, [operator.mul, operator.add]):
            total_1 += target

        if solve_equation(
            target, accumulator, numbers, [operator.mul, operator.add, concatenate]
        ):
            total_2 += target

    print(f"total of solved equations {total_1}")
    print(f"total of solved equations with concatenation {total_2}")
