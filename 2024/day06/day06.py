#!/usr/bin/env python

import sys

from utils import read_lines_as_matrix


GUARDS = ["^", ">", "v", "<"]

OBSTACLE = "#"
EMPTY = "."


def compute_direction(guard_dir):
    match guard_dir:
        case "^":
            return -1j
        case ">":
            return 1
        case "v":
            return 1j
        case "<":
            return -1


def move_guard(mat, obstacle_loc=None):
    rows = len(mat)
    cols = len(mat[0])

    # find the guard
    pos = None
    for x in range(cols):
        for y in range(rows):
            if mat[y][x] in GUARDS:
                pos = x + 1j * y

    if pos is None:
        raise ValueError("could not find the guard")

    visited = set()
    loop_visited = set()

    curr_loc = pos
    direction = compute_direction(mat[int(curr_loc.imag)][int(curr_loc.real)])

    visited.add(pos)
    loop_visited.add((pos, direction))

    while (
        curr_loc.real >= 0
        and curr_loc.imag >= 0
        and curr_loc.real < cols
        and curr_loc.imag < rows
    ):
        next_loc = curr_loc + direction
        if (
            next_loc.real < 0
            or next_loc.imag < 0
            or next_loc.real >= cols
            or next_loc.imag >= rows
        ):
            break

        while (
            mat[int(next_loc.imag)][int(next_loc.real)] == OBSTACLE
            or next_loc == obstacle_loc
        ):
            # turn 90 degrees
            direction = direction * 1j
            next_loc = curr_loc + direction

        curr_loc = next_loc

        key = (curr_loc, direction)
        if key in loop_visited:
            # found a loop
            if obstacle_loc is None:
                break
            return 1

        loop_visited.add(key)
        visited.add(curr_loc)

    if obstacle_loc is None:
        return len(visited)

    # did not get a loop, so we don't add anything
    return 0


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        lines = fp.readlines()

    mat = read_lines_as_matrix(lines)

    visits = move_guard(mat)

    loop_count = 0
    # for each empty location, see if putting an obstacle will create a loop
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            if mat[y][x] != EMPTY:
                continue

            obstacle = x + 1j * y

            loop_count += move_guard(mat, obstacle_loc=obstacle)

        sys.stdout.write(".")
        sys.stdout.flush()

    print(f"guard visited {visits} locations")
    print(f"{loop_count} locations can cause the guard to loop")
