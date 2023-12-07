#!/usr/bin/env python3

import os
import sys
from itertools import permutations

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io
from utils.parse import ints


def swap_pos(x, y, s):
    tmp = s[x]
    s[x] = s[y]
    s[y] = tmp
    return s


def swap_letter(x, y, s):
    i1 = s.index(x)
    i2 = s.index(y)
    tmp = s[i1]
    s[i1] = s[i2]
    s[i2] = tmp
    return s


def reverse(x, y, s):
    span = s[x : y + 1]
    span = span[::-1]
    return s[:x] + span + s[y + 1 :]


def rotate(right, steps, s):
    if right:
        return s[len(s) - steps :] + s[: len(s) - steps]
    else:
        return s[steps:] + s[:steps]


def rotate_letter(x, s):
    i = s.index(x)
    if i >= 4:
        i += 1
    for _ in range(i + 1):
        s = rotate(True, 1, s)
    return s


def rotate_letter_rev(x, s):
    i = s.index(x)
    # courtesy of u/rausm
    steps = i // 2 + (1 if ((i % 2) or i == 0) else 5)
    for _ in range(steps):
        s = rotate(False, 1, s)
    return s


def move(x, y, s):
    tmp = s[x]
    del s[x]
    s.insert(y, tmp)
    return s


def part1(s, filename):
    s = list(s)

    lines = io.get_lines(filename)
    for line in lines:
        if "swap position" in line:
            positions = ints(line)
            org = s[:]
            s = swap_pos(positions[0], positions[1], s)
            s2 = swap_pos(positions[1], positions[0], s[:])
            assert s2 == org
        elif "swap letter" in line:
            instr = line.split(" letter ")
            x = instr[1][0]
            y = instr[2][0]
            org = s[:]
            s = swap_letter(x, y, s)
            s2 = swap_letter(x, y, s[:])
            assert s2 == org
        elif "rotate based" in line:
            x = line[-1]
            org = s[:]
            s = rotate_letter(x, s)
            s2 = rotate_letter_rev(x, s[:])
            assert s2 == org
        elif "rotate" in line:
            dir = True if "right" in line else False
            steps = ints(line)[0]
            org = s[:]
            s = rotate(dir, steps, s)
            s2 = rotate(not dir, steps, s[:])
            assert s2 == org
        elif "reverse" in line:
            positions = ints(line)
            org = s[:]
            s = reverse(positions[0], positions[1], s)
            s2 = reverse(positions[0], positions[1], s[:])
            assert org == s2
        elif "move position" in line:
            positions = ints(line)
            org = s[:]
            s = move(positions[0], positions[1], s)
            s2 = move(positions[1], positions[0], s[:])
            assert org == s2
        else:
            raise "instruction not recognized: %s" % line

    return "".join(s)


def part2(s, filename):
    s = list(s)

    lines = io.get_lines(filename)
    lines = lines[::-1]
    for line in lines:
        if "swap position" in line:
            positions = ints(line)
            s = swap_pos(positions[1], positions[0], s)
        elif "swap letter" in line:
            instr = line.split(" letter ")
            x = instr[1][0]
            y = instr[2][0]
            s = swap_letter(x, y, s)
        elif "rotate based" in line:
            x = line[-1]
            s = rotate_letter_rev(x, s)
        elif "rotate" in line:
            dir = True if "right" in line else False
            steps = ints(line)[0]
            s = rotate(not dir, steps, s)
        elif "reverse" in line:
            positions = ints(line)
            s = reverse(positions[0], positions[1], s)
        elif "move position" in line:
            positions = ints(line)
            s = move(positions[1], positions[0], s)
        else:
            raise "instruction not recognized: %s" % line

    return "".join(s)


def part2brute(s, filename):
    for candidate in permutations(list(s)):
        attempt = "".join(part1(candidate, filename))
        if attempt == s:
            return "".join(candidate)


def main():
    assert swap_pos(0, 4, list("abcde")) == list("ebcda")
    assert swap_letter("d", "b", list("ebcda")) == list("edcba")
    assert reverse(0, 4, list("edcba")) == list("abcde")
    assert reverse(1, 3, list("abcde")) == list("adcbe")
    assert rotate(False, 1, list("abcde")) == list("bcdea")
    assert rotate(True, 2, list("abcde")) == list("deabc")
    assert move(1, 4, list("bcdea")) == list("bdeac")
    assert move(3, 0, list("bdeac")) == list("abdec")
    assert rotate_letter("b", list("abdec")) == list("ecabd")
    assert rotate_letter("d", list("ecabd")) == list("decab")

    assert part1("abcde", "example.txt") == "decab"
    print(part1("abcdefgh", "../input/2016/.txt"))

    assert swap_pos(0, 4, list("abcde")) == list("ebcda")
    assert swap_pos(4, 0, list("ebcda")) == list("abcde")
    assert swap_letter("d", "b", list("ebcda")) == list("edcba")
    assert swap_letter("d", "b", list("edcba")) == list("ebcda")
    assert rotate(False, 1, list("abcde")) == list("bcdea")
    assert rotate(True, 1, list("bcdea")) == list("abcde")
    assert reverse(1, 3, list("abcde")) == list("adcbe")
    assert reverse(1, 3, list("adcbe")) == list("abcde")
    assert reverse(1, 4, list("abcde")) == list("aedcb")
    assert reverse(1, 4, list("aedcb")) == list("abcde")
    assert move(1, 4, list("bcdea")) == list("bdeac")
    assert move(4, 1, list("bdeac")) == list("bcdea")

    assert part2("dgfaehcb", "../input/2016/.txt") == "abcdefgh"
    assert part2("fbgdceah", "../input/2016/.txt") == part2brute("fbgdceah", "../input/2016/.txt")
    print(part2brute("fbgdceah", "../input/2016/.txt"))


if __name__ == "__main__":
    sys.exit(main())
