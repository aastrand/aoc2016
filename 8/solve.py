#!/usr/bin/env python3

import re
import sys


WIDTH = 50
HEIGHT = 6


OUTPUT_MAP = {
    '#': u'\u2593',
    '.': u'\u2591'
}

def print_grid(grid):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(OUTPUT_MAP[grid[y][x]], end='')
        print()


def rect(grid, x, y):
    for yd in range(y):
        for xd in range(x):
            grid[yd][xd] = '#'
    return grid


def rotate_row(grid, y, offset):
    row = grid[y]
    grid[y] = row[-offset:] + row[:-offset]
    return grid


def rotate_column(grid, x, offset):
    col = []
    for y in range(HEIGHT):
        col.append(grid[y][x])
    col = col[-offset:] + col[:-offset]
    for y in range(HEIGHT):
        grid[y][x] = col[y]

    return grid


def make_grid(width, height):
    return [['.']*width for _ in range(height)]


# rotate row y=0 by 10
# rotate column x=0 by 1
# rect 9x1
CMD_MAP = {
    re.compile('^rect (\d+)x(\d+)$'): rect,
    re.compile('^rotate row y=(\d+) by (\d+)$'): rotate_row,
    re.compile('^rotate column x=(\d+) by (\d+)$'): rotate_column,
}


def parse(f):
    cmds = []
    for l in open(f, 'r'):
        for re, fun in CMD_MAP.items():
            m = re.match(l.strip())

            if m:
                cmds.append((fun, int(m.group(1)), int(m.group(2))))

    return cmds


def test():
    grid = make_grid(WIDTH, HEIGHT)
    grid = rect(grid, 3, 2)
    print_grid(grid)
    assert grid[0][0] == '#'
    assert grid[0][1] == '#'
    assert grid[0][2] == '#'
    assert grid[1][0] == '#'
    assert grid[1][1] == '#'
    assert grid[1][2] == '#'
    assert grid[2][2] == '.'

    grid = rotate_column(grid, 1, 1)
    print_grid(grid)
    assert grid[0][1] == '.'

    grid = rotate_row(grid, 0, 4)
    print_grid(grid)
    assert grid[0][0] == '.'
    assert grid[0][4] == '#'
    assert grid[0][5] == '.'
    assert grid[0][6] == '#'
    assert grid[0][7] == '.'


def main(f):
    test()

    grid = make_grid(WIDTH, HEIGHT)
    for cmd in parse(f):
        grid = cmd[0](grid, cmd[1], cmd[2])

    print_grid(grid)

    sum = 0
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if grid[y][x] == '#':
                sum += 1
    print(sum)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
