import pytest

from day03 import compute, tokenize


@pytest.mark.parametrize(
    "input,expected",
    [
        ("mul(3,5)", [[3, 5]]),
        ("mul(44,46)", [[44, 46]]),
        ("mul(123,4)", [[123, 4]]),
        ("mul(123,4) mul(2,2)", [[123, 4], [2, 2]]),
        ("   mul(123,4) mul (2,2)", [[123, 4]]),
        ("   mul(1234,4) mul(2,2)", [[2, 2]]),
        (
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
            [[2, 4], [5, 5], [11, 8], [8, 5]],
        ),
    ],
)
def test_tokenize(input, expected):
    result = tokenize(input)

    assert result == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("mul(3,5)", [[3, 5]]),
        ("mul(44,46)", [[44, 46]]),
        ("mul(123,4)don't()mul(1,2)", [[123, 4]]),
        ("mul(123,4)don't()do()mul(2,2)", [[123, 4], [2, 2]]),
        ("   mul(123,4)dontdo() mul (2,2)", [[123, 4]]),
        ("   mul(1234,4) mul(2,2)", [[2, 2]]),
        (
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
            [[2, 4], [5, 5], [11, 8], [8, 5]],
        ),
        (
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
            [[2, 4], [8, 5]],
        ),
    ],
)
def test_tokenize_with_disabled(input, expected):
    result = tokenize(input, can_disable=True)

    assert result == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ([[3, 5]], 15),
        ([[44, 46]], 2024),
        ([[123, 4]], 492),
        ([[123, 4], [2, 2]], 496),
        ([[2, 2]], 4),
        ([[2, 4], [5, 5], [11, 8], [8, 5]], 161),
    ],
)
def test_compute(input, expected):
    result = compute(input)

    assert result == expected
