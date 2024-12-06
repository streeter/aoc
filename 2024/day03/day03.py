#!/usr/bin/env python

from functools import reduce
from operator import mul

from utils import Scanner


class MulScanner(Scanner):
    MUL = "mul"
    DO = "do"
    DONT = "don't"

    def main(self, can_disable=False):
        tokens = []

        enabled = True

        while not self.eos():
            self.skip_whitespace()
            c = self.peek()
            if not c:
                break

            operations = f"({self.MUL}|{self.DONT}|{self.DO})"
            if not self.exists(operations):
                break

            # Move forward to the next spot
            self.scan_to(operations)

            oper = self.scan(operations)
            if not oper:
                break

            paren = self.get()
            if paren != "(":
                # start over
                continue

            if oper == self.MUL:
                # Get the first number
                first = self.scan("[0-9]{1,3}")
                if not first:
                    continue

                sep = self.get()
                if sep != ",":
                    continue

                second = self.scan("[0-9]{1,3}")
                if not second:
                    continue
            elif oper == self.DONT:
                pass
            elif oper == self.DO:
                pass
            else:
                # Unknown operator
                continue

            paren = self.get()
            if paren != ")":
                continue

            if oper == self.MUL:
                if enabled:
                    tokens += [[int(first), int(second)]]
            elif oper == self.DONT:
                enabled = False
            elif oper == self.DO:
                enabled = True

        return tokens


def tokenize(line, can_disable=False):
    scanner = MulScanner(line)

    tokens = scanner.main(can_disable=can_disable)

    return tokens


def compute(tokens):
    return sum([mul(*nums) for nums in tokens])


if __name__ == "__main__":
    with open("input.txt", "r") as fp:
        lines = fp.readlines()

    line = reduce(lambda x, y: x + y, lines)

    tokens = tokenize(line, can_disable=True)

    result = compute(tokens)

    print(f"line value is {result}")
