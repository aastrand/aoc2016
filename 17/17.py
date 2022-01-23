#!/usr/bin/env python3

import hashlib
import os
import sys
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils.grid import OFFSETS_STRAIGHT, Grid

DIRECTIONS = {"U": (0, -2), "D": (0, 2), "L": (-2, 0), "R": (2, 0)}


def hash(s):
    return hashlib.md5(str.encode(s)).hexdigest()


def doors(passcode, path):
    digest = hash("%s%s" % (passcode, "".join(path)))
    return {
        "U": int(digest[0], 16) > 10,  # up
        "D": int(digest[1], 16) > 10,  # down
        "L": int(digest[2], 16) > 10,  # left
        "R": int(digest[3], 16) > 10,  # right
    }


VAULT = [
    "#########",
    "# | | | #",
    "#-#-#-#-#",
    "# | | | #",
    "#-#-#-#-#",
    "# | | | #",
    "#-#-#-#-#",
    "# | | | #",
    "#########",
]


def build_graph():
    data = {}
    for y, line in enumerate(VAULT):
        for x, char in enumerate(line):
            data[(x, y)] = char
    grid = Grid(data, 0, len(VAULT[0]), 0, len(VAULT))

    graph = defaultdict(list)
    for y in range(grid.maxY + 1):
        for x in range(grid.maxX + 1):
            pos = (x, y)
            if grid.data.get(pos) == " ":
                for o in OFFSETS_STRAIGHT:
                    n = (x + o[0], y + o[1])
                    val = data.get(n)
                    if val == "|" or val == "-":
                        graph[pos].append((pos[0] + (o[0] * 2), pos[1] + (o[1] * 2)))

    return graph


def find(passcode, graph, cur, target, path, cmp=lambda a, b: a < b):
    if cur == target:
        return path, len(path)

    door_status = doors(passcode, path)

    opt = None
    opt_path = None
    for dir, open in door_status.items():
        if open:
            next = (cur[0] + DIRECTIONS[dir][0], cur[1] + DIRECTIONS[dir][1])
            if next in graph.get(cur, []):
                new_path, length = find(
                    passcode, graph, next, target, path + [dir], cmp
                )
                if length is not None and (opt is None or cmp(length, opt)):
                    opt = length
                    opt_path = new_path

    return opt_path, opt


def part1(passcode):
    graph = build_graph()
    path, _ = find(passcode, graph, (1, 1), (7, 7), [])

    return "".join(path)


def part2(passcode):
    graph = build_graph()
    _, length = find(passcode, graph, (1, 1), (7, 7), [], lambda a, b: a > b)

    return length


def main():
    open = doors("hijkl", [])
    assert open["U"]
    assert open["D"]
    assert open["L"]
    assert not open["R"]

    open = doors("hijkl", ["D"])
    assert open["U"]
    assert not open["D"]
    assert open["L"]
    assert open["R"]

    open = doors("hijkl", ["DR"])
    assert not open["U"]
    assert not open["D"]
    assert not open["L"]
    assert not open["R"]

    open = doors("hijkl", ["DU"])
    assert not open["U"]
    assert not open["D"]
    assert not open["L"]
    assert open["R"]

    open = doors("hijkl", ["DUR"])
    assert not open["U"]
    assert not open["D"]
    assert not open["L"]
    assert not open["R"]

    assert part1("ihgpwlah") == "DDRRRD"
    assert part1("kglvqrro") == "DDUDRLRRUDRD"
    assert part1("ulqzkmiv") == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"

    print(part1("udskfozm"))

    assert part2("ihgpwlah") == 370
    assert part2("kglvqrro") == 492
    assert part2("ulqzkmiv") == 830
    print(part2("udskfozm"))


if __name__ == "__main__":
    sys.exit(main())
