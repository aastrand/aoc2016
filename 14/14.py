#!/usr/bin/env python3

import hashlib
import os
import sys
from collections import OrderedDict, defaultdict

from sympy import Or

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


def hash(s):
    return hashlib.md5(str.encode(s)).hexdigest()


def stretch(s):
    for _ in range(2016):
        s = hashlib.md5(str.encode(s)).hexdigest()

    return s


def count(s, n, candidates, fives):
    prev = None
    count = 1
    for i, char in enumerate(s):
        if prev == char:
            count += 1
        else:
            count = 1

        if count == 3:
            found = candidates.get(n)
            if found is None:
                candidates[n] = prev
        elif count == 5:
            fives[prev].append(n)

        prev = char


def solve(salt, should_stretch=False):
    fives = defaultdict(list)
    candidates = OrderedDict()
    for i in range(30000):
        h = hash("%s%s" % (salt, i))

        if should_stretch:
            h = stretch(h)

        count(h, i, candidates, fives)

    keys = set()
    for c in candidates:
        for chars in candidates[c]:
            for others in fives.get(chars, []):
                if 0 < others - c <= 1000:
                    keys.add(c)
                    break

        if len(keys) == 64:
            return c

    raise "should not happen"


def main():
    assert hash("abc816") == "3aeeeee1367614f3061d165a5fe3cac3"

    fives = defaultdict(list)
    candidates = OrderedDict()
    count("eeeee1367614f30000061d165a5fe3caaaaa", 0, candidates, fives)
    assert len(fives.keys()) == 3
    assert fives["e"] == [0]
    assert fives["a"] == [0]
    assert fives["0"] == [0]

    candidates = OrderedDict()
    count("eecefd1367614ffdf3061d165a5fe3cfbaaa", 0, candidates, fives)
    assert candidates[0] == "a"
    candidates = OrderedDict()
    count("eeefd1367614ffdf3061d165a5fe3cfbaaa", 0, candidates, fives)
    assert candidates[0] == "e"

    fives = defaultdict(list)
    candidates = OrderedDict()
    count("4fc7df57777400b3eeef5350a6eecbdf", 0, candidates, fives)
    assert candidates[0] == "7"

    input = "ahsbgdzn"
    assert solve("abc") == 22728
    print(solve(input))

    s = hash("abc0")
    assert s == "577571be4de9dcce85a041ba0410f29f"
    assert stretch(s) == "a107ff634856bb300138cac6568c0f24"

    assert solve("abc", True) == 22551
    print(solve(input, True))


if __name__ == "__main__":
    sys.exit(main())
