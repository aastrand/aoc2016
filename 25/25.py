#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


def part1(a=0):
    d = a + 2572

    while "0b101010101010" != bin(d):
        a += 1
        d = a + 2572

    return a


def main():
    print(part1())


if __name__ == "__main__":
    sys.exit(main())
