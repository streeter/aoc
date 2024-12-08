#!/usr/bin/env python

from collections import defaultdict

from utils import read_input_lines, read_lines_as_matrix


def is_valid_coordinate(x, y, max_x, max_y):
    return 0 <= x < max_x and 0 <= y < max_y


def find_word(mat, max_x, max_y, word, index, x, y, dir_x, dir_y):
    if index == len(word):
        return True

    if not is_valid_coordinate(x, y, max_x, max_y):
        return False

    if word[index] != mat[x][y]:
        return False

    # recurse
    return find_word(
        mat, max_x, max_y, word, index + 1, x + dir_x, y + dir_y, dir_x, dir_y
    )


def search_matrix(mat, word):
    results = []
    max_x = len(mat)
    max_y = len(mat[0])

    # Directions for 8 possible movements
    directions = [
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]

    for x in range(max_x):
        for y in range(max_y):
            # Check if the first character matches
            if mat[x][y] != word[0]:
                continue

            for dir_x, dir_y in directions:
                if find_word(mat, max_x, max_y, word, 0, x, y, dir_x, dir_y):
                    results.append([x, y])

    return results


def search_matrix_for_x(mat, word):
    results = []

    grid = defaultdict(lambda: ".")
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            grid[(x, y)] = mat[x][y]

    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if grid[(x, y)] != "A":
                continue

            matches = 0
            if grid[(x - 1, y - 1)] == "M" and grid[(x + 1, y + 1)] == "S":
                matches += 1
            if grid[(x - 1, y - 1)] == "S" and grid[(x + 1, y + 1)] == "M":
                matches += 1
            if grid[(x + 1, y - 1)] == "M" and grid[(x - 1, y + 1)] == "S":
                matches += 1
            if grid[(x + 1, y - 1)] == "S" and grid[(x - 1, y + 1)] == "M":
                matches += 1
            if matches == 2:
                results.append([x, y])

    return results


if __name__ == "__main__":
    lines = read_input_lines()

    mat = read_lines_as_matrix(lines)

    results = search_matrix_for_x(mat, "MAS")

    print(f"found {len(results)} results")
