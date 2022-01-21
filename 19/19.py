#!/usr/bin/env python3

import os
import sys
from math import floor

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


class Elf:
    def __init__(self, num, presents):
        self.num = num
        self.presents = presents
        self.next = None

    def __repr__(self):
        return "%s, %s" % (self.num, self.presents)


def part1(num):
    head = Elf(1, 1)
    cur = head
    for i in range(2, num + 1):
        node = Elf(i, 1)
        cur.next = node
        cur = node
    cur.next = head

    has_present = num

    cur = head
    while has_present > 1:
        cur.presents += cur.next.presents
        cur.next = cur.next.next
        has_present -= 1
        cur = cur.next

    return cur.num


def part2(num):
    head = Elf(1, 1)
    cur = head
    opposite = None
    for i in range(2, num + 1):
        node = Elf(i, 1)
        if i == (num // 2):
            opposite = node
        cur.next = node
        cur = node
    cur.next = head

    has_present = num

    cur = head
    while has_present > 1:
        cur.presents += opposite.next.presents
        opposite.next = opposite.next.next
        has_present -= 1
        cur = cur.next
        if has_present % 2 == 0:
            opposite = opposite.next

    return cur.num


def main():
    assert part1(5) == 3
    print(part1(3004953))

    assert part2(5) == 2
    print(part2(3004953))


if __name__ == "__main__":
    sys.exit(main())
