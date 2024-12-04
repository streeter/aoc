#!/usr/bin/env python


def format_lists(lines):
    # group lines into lists
    number_lines = [line.strip() for line in lines if line.strip()]
    numbers = [[int(num) for num in line.split()] for line in number_lines]

    # pivot and sort the matrix
    pivoted = [[row[i] for row in numbers] for i in range(2)]

    return pivoted


def total_distance(lists):
    # sort the lists
    sorted_lists = [sorted(nums) for nums in lists]

    # get the distances
    total_distance = sum(
        [
            abs(sorted_lists[0][i] - sorted_lists[1][i])
            for i in range(len(sorted_lists[0]))
        ]
    )

    print(f"total distance: {total_distance}")


def similarity(lists):
    left = lists[0]
    right = lists[1]

    scores = [num * right.count(num) for num in left]

    score = sum(scores)

    print(f"similary score: {score}")


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        lines = fp.readlines()

    lists = format_lists(lines)

    total_distance(lists)

    similarity(lists)
