import operator

import pytest

from day07 import solve_equation, concatenate


BASE_OPERATIONS = [operator.mul, operator.add]
EXTENDED_OPS = BASE_OPERATIONS + [concatenate]


@pytest.mark.parametrize(
    "first,second,expected",
    [
        [1, 2, 12],
        [0, 1, 1],
        [11, 123, 11123],
    ],
)
def test_concatenate(first, second, expected):
    assert concatenate(first, second) == expected


@pytest.mark.parametrize(
    "target,numbers,operations,solvable",
    [
        # base ops
        [190, [10, 19], BASE_OPERATIONS, True],
        [3267, [81, 40, 27], BASE_OPERATIONS, True],
        [292, [11, 6, 16, 20], BASE_OPERATIONS, True],
        [10, [5], BASE_OPERATIONS, False],
        [10, [5, 1], BASE_OPERATIONS, False],
        [192, [17, 8, 14], BASE_OPERATIONS, False],
        [156, [15, 6], BASE_OPERATIONS, False],
        # extended
        [156, [15, 6], EXTENDED_OPS, True],
        [7290, [6, 8, 6, 15], EXTENDED_OPS, True],
        [192, [17, 8, 14], EXTENDED_OPS, True],
    ],
)
def test_solve_equation(target, numbers, operations, solvable):
    accumulator, *rest = numbers

    assert solve_equation(target, accumulator, rest, operations) == solvable
