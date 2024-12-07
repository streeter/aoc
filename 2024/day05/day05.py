#!/usr/bin/env python

from functools import cmp_to_key


from utils import middle_of_list, split_and_cast


def is_correctly_ordered(update, rules):
    for rule in rules:
        first, second = rule
        try:
            first_pos = update.index(first)
        except ValueError:
            continue

        try:
            second_pos = update.index(second)
        except ValueError:
            continue

        if first_pos < second_pos:
            continue

        return False

    return True


def fix_ordering(update, rules):
    if is_correctly_ordered(update, rules):
        return update

    def compare_with_rules(item_a, item_b):
        for rule in rules:
            if item_a not in rule:
                # This rule doesn't apply
                continue
            if item_b not in rule:
                # this rule doesn't apply
                continue

            first, _ = rule

            # How should these be sorted?
            if first == item_a:
                return -1
            if first == item_b:
                return 1

        # Leave them alone
        return 0

    return sorted(update, key=cmp_to_key(compare_with_rules))


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        lines = fp.readlines()

    rules = [split_and_cast(line, "|") for line in lines if "|" in line]
    page_updates = [split_and_cast(line, ",") for line in lines if "," in line]

    # split up the lists
    ordered, unordered = [], []
    for update in page_updates:
        (unordered, ordered)[is_correctly_ordered(update, rules)].append(update)

    # fix the unordered lists
    unordered_updates = [fix_ordering(update, rules) for update in unordered]

    # Get the middle number from each and sum
    ordered_total = sum([middle_of_list(update) for update in ordered])
    unordered_total = sum([middle_of_list(update) for update in unordered_updates])

    print(f"sum of correctly ordered middle numbers {ordered_total}")
    print(f"sum of incorrectly ordered middle numbers {unordered_total}")
