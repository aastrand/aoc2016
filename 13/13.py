#!/usr/bin/env python3

import os
import sys
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils.graph import dijkstra
from utils.grid import OFFSETS_STRAIGHT, Grid


def get_grid(input, maxX, maxY):
    data = {}
    for y in range(maxX):
        for x in range(maxY):
            val = x * x + 3 * x + 2 * x * y + y + y * y
            val += input
            bits = sum([int(b) for b in bin(val)[2:]])
            data[(x, y)] = "." if bits % 2 == 0 else "#"

    return Grid(data, 0, maxX, 0, maxY)


def build_graph(grid):
    graph = defaultdict(list)
    for y in range(grid.maxY + 1):
        for x in range(grid.maxX + 1):
            for o in OFFSETS_STRAIGHT:
                n = (x + o[0], y + o[1])
                val = grid.data.get(n)
                if val == ".":
                    graph[(x, y)].append(n)

    return graph


def part1(input, target):
    grid = get_grid(input, target[0] + 10, target[1] + 10)
    graph = build_graph(grid)

    path, _, _ = dijkstra(graph, (1, 1), target)

    return len(path) - 1


def get_path(n, prev):
    path = []
    u = n
    if u in prev:
        while u:
            path.insert(0, u)
            u = prev.get(u)

    return path


def bfs(start, graph, max):
    visited = set()
    q = []

    q.append(start)
    visited.add(start)

    _, _, prev = dijkstra(graph, start, start)

    while len(q) > 0:
        cur = q.pop(0)
        for n in graph.get(cur, []):
            if not n in visited:
                path = get_path(n, prev)
                if len(path) - 1 <= max:
                    q.append(n)
                    visited.add(n)

    return visited


def part2(input, size):
    grid = get_grid(input, size, size)
    graph = build_graph(grid)

    visited = bfs((1, 1), graph, 50)

    return len(visited)


def main():
    assert part1(10, (7, 4)) == 11
    print(part1(1364, (31, 39)))

    print(part2(1364, 100))


if __name__ == "__main__":
    sys.exit(main())
