import pytest

from utils import read_lines_as_matrix, middle_of_list, chars, ints


def test_read_lines_as_matrix():
    lines = ["..X...", ".SAMX."]

    mat = read_lines_as_matrix(lines)

    assert mat == [[".", ".", "X", ".", ".", "."], [".", "S", "A", "M", "X", "."]]


def test_middle_of_list():
    assert middle_of_list([1, 2, 3]) == 2
    assert middle_of_list([1, 2, 3, 4, 5]) == 3
    assert middle_of_list([1, 2, 3, 4]) == 3

    assert middle_of_list(["1", "2", "3", "4", "5"]) == "3"


@pytest.mark.parametrize(
    "input,expected",
    [
        ["123: 11, 12,13", [123, 11, 12, 13]],
        ["-2 3 4", [-2, 3, 4]],
    ],
)
def test_ints(input, expected):
    assert ints(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        [".A.a.A.0.", ["A", "a", "0"]],
        ["AA0", ["A", "0"]],
    ],
)
def test_chars(input, expected):
    assert chars(input) == expected
