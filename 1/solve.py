#!/usr/bin/env python3

import sys


def parse(f):
    cmds = []
    for l in open(f, 'r'):
        cmds.extend([(c.strip()[0], int(c.strip()[1:])) for c in l.strip().split(',')])

    return cmds


def print_grid(grid, pos=None, clear=False):
    x_min = x_max = y_min = y_max = 0

    for key in grid.keys():
        if x_min > key[0]:
            x_min = key[0]
        if x_max < key[0]:
            x_max = key[0]
        if y_min > key[1]:
            y_min = key[1]
        if y_max < key[1]:
            y_max = key[1]

    if clear:
        print('\033c')
    for y in range(y_min, y_max+1):
        for x in range(x_min, x_max+1):
            if (x, y) == pos:
                print('S', end='')
            else:
                print(grid.get((x, y), ' '), end='')
        print()


def main(f):
    cmds = parse(f)

    offsets = [
        (0, -1), # N
        (1, 0),
        (0, 1),
        (-1, 0)
    ]
    i = 0

    pos = [0, 0]
    grid = {}
    grid[tuple(pos)] = 'X'
    twice = False

    for cmd in cmds:
        if cmd[0] == 'R':
            i += 1
        else:
            i -= 1
        i = i % 4

        for n in range(0, cmd[1]):
            pos[0] += offsets[i][0]
            pos[1] += offsets[i][1]
            if not twice and grid.get(tuple(pos)) != None:
                print('twice', abs(pos[0]) + abs(pos[1]))
                twice = True
                grid[tuple(pos)] = 'T'
            else:
                grid[tuple(pos)] = 'X'

    print(abs(pos[0]) + abs(pos[1]))
    print_grid(grid, (0, 0))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
