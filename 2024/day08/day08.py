#!/usr/bin/env python

from collections import defaultdict
from itertools import combinations
import re

from utils import read_input_lines


def compute_antinodes(
    pos1: tuple[int, int], pos2: tuple[int, int]
) -> list[tuple[int, int]]:
    row_dist = pos2[0] - pos1[0]
    col_dist = pos2[1] - pos1[1]

    return [
        an
        for an in [
            (pos1[0] - row_dist, pos1[1] - col_dist),
            (pos2[0] + row_dist, pos2[1] + col_dist),
        ]
    ]


def compute_all_antinodes(
    max_row: int, max_col: int, positions: list[tuple[int, int]]
) -> set[tuple[int, int]]:
    if len(positions) < 2:
        return set()

    antinodes = set(positions)

    combos = combinations(positions, 2)
    for pos1, pos2 in combos:
        # distance apart
        row_dist = pos2[0] - pos1[0]
        col_dist = pos2[1] - pos1[1]

        next = (pos1[0] - row_dist, pos1[1] - col_dist)
        while next[0] >= 0 and next[0] < max_row and next[1] >= 0 and next[1] < max_col:
            antinodes.add(next)
            next = (next[0] - row_dist, next[1] - col_dist)

        next = (pos2[0] + row_dist, pos2[1] + col_dist)
        while next[0] >= 0 and next[0] < max_row and next[1] >= 0 and next[1] < max_col:
            antinodes.add(next)
            next = (next[0] + row_dist, next[1] + col_dist)

    return antinodes


if __name__ == "__main__":
    mat = read_input_lines()

    max_col = len(mat[0])
    max_row = len(mat)
    freqs = defaultdict[str, list[tuple[int, int]]](list)

    pattern = re.compile(r"^[A-Za-z0-9]$")

    for row, content in enumerate(mat):
        for col, char in enumerate(content):
            if pattern.match(char):
                freqs[char].append((row, col))

    antinodes = defaultdict(set)

    # for each freq, find antinodes
    for freq, positions in freqs.items():
        antinodes[freq].update(compute_all_antinodes(max_row, max_col, positions))

    all_locations = set()
    for positions in antinodes.values():
        all_locations.update(positions)

    total = len(all_locations)

    print(f"total antinode locations {total}")
