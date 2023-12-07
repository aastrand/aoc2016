#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io
from utils.parse import ints


def solve(filename, part2=False):
    lines = io.get_lines(filename)
    discs = []
    for line in lines:
        d = ints(line)
        discs.append((d[1], d[3]))

    if part2:
        discs.append((11, 0))

    t = 0
    while True:
        for i, d in enumerate(discs):
            if (d[1] + i + t + 1) % d[0] != 0:
                break
        else:
            return t

        t += 1


def main():
    assert solve("example.txt") == 5
    print(solve("../input/2016/.txt"))
    print(solve("../input/2016/.txt", True))


if __name__ == "__main__":
    sys.exit(main())
