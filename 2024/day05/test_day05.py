import pytest

from day05 import is_correctly_ordered, fix_ordering


EXAMPLE_RULES = [
    [47, 53],
    [97, 13],
    [97, 61],
    [97, 47],
    [75, 29],
    [61, 13],
    [75, 53],
    [29, 13],
    [97, 29],
    [53, 29],
    [61, 53],
    [97, 53],
    [61, 29],
    [47, 13],
    [75, 47],
    [97, 75],
    [47, 61],
    [75, 61],
    [47, 29],
    [75, 13],
    [53, 13],
]


@pytest.mark.parametrize(
    "update,rules,expected",
    [
        [
            [75, 47, 61, 53, 29],
            EXAMPLE_RULES,
            True,
        ],
        [[97, 61, 53, 29, 13], EXAMPLE_RULES, True],
        [[75, 29, 13], EXAMPLE_RULES, True],
        [[75, 97, 47, 61, 53], EXAMPLE_RULES, False],
        [[61, 13, 29], EXAMPLE_RULES, False],
        [[97, 13, 75, 29, 47], EXAMPLE_RULES, False],
        [[75, 97, 47, 61, 53], [[97, 75]], False],
        [[61, 13, 29], [[29, 13]], False],
    ],
)
def test_is_correctly_ordered(update, rules, expected):
    assert is_correctly_ordered(update, rules) == expected


@pytest.mark.parametrize(
    "update,rules,expected",
    [
        [[97, 61, 53, 29, 13], EXAMPLE_RULES, [97, 61, 53, 29, 13]],
        [[75, 97, 47, 61, 53], EXAMPLE_RULES, [97, 75, 47, 61, 53]],
        [[61, 13, 29], EXAMPLE_RULES, [61, 29, 13]],
        [[97, 13, 75, 29, 47], EXAMPLE_RULES, [97, 75, 47, 29, 13]],
        [[97, 13, 75, 29, 47], [], [97, 13, 75, 29, 47]],
        [[61, 13, 29], [[29, 13]], [61, 29, 13]],
    ],
)
def test_fix_ordering(update, rules, expected):
    assert fix_ordering(update, rules) == expected
