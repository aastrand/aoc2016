#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


def part1(filename):
    lines = io.get_lines(filename)

    return 0


def part2(filename):
    lines = io.get_lines(filename)

    return 0


def main():
    assert part1("example.txt") == 0
    print(part1("input.txt"))

    assert part2("example.txt") == 0
    print(part2("input.txt"))


if __name__ == "__main__":
    sys.exit(main())
