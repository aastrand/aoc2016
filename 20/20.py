#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


def solve(filename, max_ip):
    lines = io.get_lines(filename)
    ranges = []
    for line in lines:
        r = line.split("-")
        ranges.append([int(r[0]), int(r[1])])

    ranges.sort(key=lambda n: n[0])
    merged = True
    head = 0
    while merged:
        merged = False
        remove = None
        for i in range(head, len(ranges) - 1):
            cur = ranges[i]
            next = ranges[i + 1]
            if cur[1] + 1 >= (next[0]):
                if next[1] > cur[1]:
                    cur[1] = next[1]

                merged = True
                remove = i + 1
                head = i
                break

        if remove:
            del ranges[remove]

    sum = 0
    for i in range(len(ranges) - 1):
        cur = ranges[i]
        next = ranges[i + 1]
        sum += next[0] - cur[1] - 1

    sum += max_ip - ranges[-1][1]

    return ranges[0][1] + 1, sum


def main():
    test = solve("example.txt", 9)
    assert test[0] == 3
    assert test[1] == 2

    r = solve("input.txt", 4294967295)
    print(r[0])
    print(r[1])


if __name__ == "__main__":
    sys.exit(main())
