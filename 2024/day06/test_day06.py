import pytest

from day06 import move_guard
from utils import Matrix


@pytest.mark.parametrize(
    "input,expected",
    [
        [[["^"]], 1],
        [
            [
                ["#", "."],
                [".", "."],
                [".", "."],
                ["^", "."],
            ],
            4,
        ],
        [
            [
                ["#", "."],
                [".", "#"],
                [".", "."],
                ["^", "."],
            ],
            3,
        ],
        [
            [
                ["#", ".", "."],
                [".", ".", "#"],
                [".", ".", "."],
                ["^", ".", "."],
            ],
            6,
        ],
        [
            [
                ["#", "#", ".", "."],
                [".", ".", ".", "#"],
                ["^", ".", ".", "."],
                ["#", ".", ".", "."],
                [".", ".", "#", "."],
            ],
            8,
        ],
    ],
)
def test_move_guard(input, expected):
    mat = Matrix(input)

    result = move_guard(mat)
    assert result == expected
