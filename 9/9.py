#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


# kudos to u/blockingthesky
def decompress(s, recursive=False):
    if "(" not in s:
        return len(s)

    ret = 0
    while "(" in s:
        # cut way first until next marker
        ret += s.find("(")
        s = s[s.find("(") :]

        # extract marker
        marker = s[1 : s.find(")")].split("x")
        # cut away the actual marker
        s = s[s.find(")") + 1 :]

        if recursive:
            # recurse into the string
            ret += decompress(s[: int(marker[0])], True) * int(marker[1])
        else:
            # string * number repeats the string, add the length of that temp
            ret += len(s[: int(marker[0])]) * int(marker[1])

        # cut away the unrepeated part
        s = s[int(marker[0]) :]

    # add the tail
    ret += len(s)

    return ret


def part1(filename):
    lines = io.get_lines(filename)

    sum = 0
    for line in lines:
        sum += decompress(line)

    return sum


def part2(filename):
    lines = io.get_lines(filename)

    sum = 0
    for line in lines:
        sum += decompress(line, True)

    return sum


def main():
    assert part1("example.txt") == 6 + 7 + 9 + 11 + 6 + 18
    print(part1("input.txt"))

    assert decompress("(27x12)(20x12)(13x14)(7x10)(1x12)A", True) == 241920
    print(part2("input.txt"))


if __name__ == "__main__":
    sys.exit(main())
