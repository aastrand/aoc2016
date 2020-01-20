#!/usr/bin/env python3

import sys


def parse(f):
    cmds = []
    for l in open(f, 'r'):
        cmds.append(l.strip())

    return cmds


OFFSET_MAP = {
    'U': (0, -1),
    'D': (0, 1),
    'R': (1, 0),
    'L': (-1, 0)
}
def offset_pos(pos, offset):
    return (pos[0]+offset[0], pos[1]+offset[1])


def get_code(grid, cmds, start_pos):
    code = []
    pos = start_pos

    for l in cmds:
        for d in l:
            offset = OFFSET_MAP[d]
            new_pos = offset_pos(pos, offset)
            if grid.get(new_pos):
                pos = new_pos
        code.append(grid[pos])

    return code


def main(f):
    cmds = parse(f)

    grid = {
        (0, 0): '1',
        (1, 0): '2',
        (2, 0): '3',

        (0, 1): '4',
        (1, 1): '5',
        (2, 1): '6',

        (0, 2): '7',
        (1, 2): '8',
        (2, 2): '9',

    }

    code = get_code(grid, cmds, (1, 1))
    print(''.join(code))

    grid = {
        (0, 0): '2',
        (1, 0): '3',
        (2, 0): '4',

        (0, 1): '6',
        (1, 1): '7',
        (2, 1): '8',

        (0, 2): 'A',
        (1, 2): 'B',
        (2, 2): 'C',

        (1, -1): '1',
        (-1, 1): '5',
        (3, 1): '9',
        (1, 3): 'D',
    }

    code = get_code(grid, cmds, (-1, 1))
    print(''.join(code))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
