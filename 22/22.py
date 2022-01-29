#!/usr/bin/env python3

import os
import sys
from collections import namedtuple

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io
from utils.grid import Grid, print_grid

Node = namedtuple("Node", "pos size used avail use")


def get_nodes(lines):
    nodes = []
    for line in lines:
        if "/dev/grid" in line:
            parts = list(filter(lambda p: p != "", line.split(" ")))
            pos = parts[0].split("/")[-1].split("-")
            nodes.append(
                Node(
                    (int(pos[1][1:]), int(pos[2][1:])),
                    int(parts[1][:-1]),
                    int(parts[2][:-1]),
                    int(parts[3][:-1]),
                    int(parts[4][:-1]),
                )
            )

    return nodes


def part1(filename):
    nodes = get_nodes(io.get_lines(filename))

    pairs = set()
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if nodes[i].used > 0 and i != j and nodes[i].used <= nodes[j].avail:
                pairs.add((i, j))

    return len(pairs)


def part2(filename):
    nodes = get_nodes(io.get_lines(filename))

    maxX = 0
    maxY = 0
    for node in nodes:
        if node.pos[0] > maxX:
            maxX = node.pos[0]
        if node.pos[1] > maxY:
            maxY = node.pos[1]
    goal = (maxX, 0)

    data = {}
    for node in nodes:
        x, y = node.pos
        if (x, y) == goal:
            data[(x, y)] = "G"
        elif node.size > 100:
            data[(x, y)] = "#"
        elif node.used == 0:
            data[(x, y)] = "_"
        else:
            data[(x, y)] = "."

    grid = Grid(data, 0, maxX + 1, 0, maxY + 1)
    print_grid(grid)

    return "do it by hand, example is 7, my grid is 233 (see notes.txt)"


def main():
    print(part1("input.txt"))

    print(part2("example.txt"))
    print(part2("input.txt"))


if __name__ == "__main__":
    sys.exit(main())
