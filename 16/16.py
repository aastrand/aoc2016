#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


def dragon(a):
    b = a[::-1]
    b = b.replace("0", "3")
    b = b.replace("1", "0")
    b = b.replace("3", "1")

    return "%s0%s" % (a, b)


def checksum(s):
    while len(s) % 2 != 1:
        sum = []
        for i in range(0, len(s), 2):
            sum.append("1" if s[i] == s[i + 1] else "0")
        s = "".join(sum)

    return s


def solve(s, length):
    while len(s) < length:
        s = dragon(s)

    s = s[:length]

    return checksum(s)


def main():
    assert dragon("1") == "100"
    assert dragon("0") == "001"
    assert dragon("11111") == "11111000000"
    assert dragon("111100001010") == "1111000010100101011110000"

    assert checksum("110010110100") == "100"

    assert solve("10000", 20) == "01100"
    print(solve("10111011111001111", 272))
    print(solve("10111011111001111", 35651584))


if __name__ == "__main__":
    sys.exit(main())
