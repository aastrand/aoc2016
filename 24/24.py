#!/usr/bin/env python3

import os
import sys
from collections import defaultdict
from itertools import permutations

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io
from utils.graph import dijkstra
from utils.grid import OFFSETS_STRAIGHT, Grid, get_grid, print_grid


def build_graph(grid):
    graph = defaultdict(list)
    points = []
    for y in range(grid.maxY + 1):
        for x in range(grid.maxX + 1):
            cur = grid.data.get((x, y))
            if cur is not None and cur != "#":
                if cur != ".":
                    points.append((cur, (x, y)))

                for o in OFFSETS_STRAIGHT:
                    n = (x + o[0], y + o[1])
                    val = grid.data.get(n)
                    if val is not None and val != "#":
                        graph[(x, y)].append(n)

    return graph, points


def get_path(n, prev):
    path = []
    u = n
    if u in prev:
        while u:
            path.insert(0, u)
            u = prev.get(u)

    return path


def solve(filename, ret=False):
    grid = get_grid(io.get_lines(filename))
    graph, points = build_graph(grid)

    to_visit = []
    for p in points:
        if p[0] == "0":
            start = p
        else:
            to_visit.append(p)

    prevs = {}
    for p in points:
        _, _, prev = dijkstra(graph, p[1], None)
        prevs[p[1]] = prev

    dist = {}
    min = sys.maxsize
    for p in permutations(to_visit):
        p = [start] + list(p)
        if ret:
            p = p + [start]

        s = 0
        for i in range(len(p) - 1):
            pair = (p[i][1], p[i + 1][1])
            if pair not in dist:
                path = get_path(p[i][1], prevs[p[i + 1][1]])
                dist[pair] = len(path) - 1
            s += dist[pair]
        if s < min:
            min = s

    return min


def main():
    assert solve("example.txt") == 14
    print(solve("../input/2016/.txt"))

    print(solve("../input/2016/.txt", True))


if __name__ == "__main__":
    sys.exit(main())
