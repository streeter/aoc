import pytest

from day08 import compute_antinodes, compute_all_antinodes


@pytest.mark.parametrize(
    "pos1,pos2,expected",
    [
        [(3, 4), (5, 5), [(1, 3), (7, 6)]],
        [(3, 4), (4, 8), [(2, 0), (5, 12)]],
        [(5, 5), (4, 8), [(6, 2), (3, 11)]],
    ],
)
def test_compute_antinodes(pos1, pos2, expected):
    assert compute_antinodes(pos1, pos2) == expected


@pytest.mark.parametrize(
    "max_row,max_col,positions,expected",
    [
        [
            50,
            50,
            [(11, 49), (22, 35), (36, 18), (37, 22)],
            {
                (35, 14),
                (44, 7),
                (38, 26),
                (43, 46),
                (34, 10),
                (37, 22),
                (39, 30),
                (7, 48),
                (33, 6),
                (42, 42),
                (41, 38),
                (33, 21),
                (22, 35),
                (36, 18),
                (40, 34),
                (11, 49),
                (32, 2),
            },
        ]
    ],
)
def test_compute_all_antinodes(max_row, max_col, positions, expected):
    assert compute_all_antinodes(max_row, max_col, positions) == expected
