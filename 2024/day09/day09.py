#!/usr/bin/env python

from utils import read_input_lines


if __name__ == "__main__":
    lines = read_input_lines()

    line = lines[0]

    occupied = []
    free = []
    for pos, len in enumerate(line):
        if pos % 2 == 0:
            for i in range(0, int(len)):
                pass

    # TODO
    sum_lengths(lines)
