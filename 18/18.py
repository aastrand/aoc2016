#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


def count(cur):
    return sum([1 if c == "." else 0 for c in cur]) - 2


def solve(initial, n):

    cur = ".%s." % initial

    traps = count(cur)
    for _ in range(n - 1):
        next = ["."]
        for i in range(1, len(cur) - 1):
            above = cur[i - 1 : i + 2]

            # Its left and center tiles are traps, but its right tile is not.
            # Its center and right tiles are traps, but its left tile is not.
            # Only its left tile is a trap.
            # Only its right tile is a trap.
            if above == "^^." or above == ".^^" or above == "^.." or above == "..^":
                next.append("^")
            else:
                next.append(".")

        next.append(".")
        cur = "".join(next)
        traps += count(cur)

    return traps


def main():
    input = "^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^."

    assert solve("..^^.", 3) == 6
    assert solve(".^^.^.^^^^", 10) == 38
    print(solve(input, 40))
    print(solve(input, 400000))


if __name__ == "__main__":
    sys.exit(main())
