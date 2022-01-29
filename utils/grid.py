from collections import namedtuple

RIGHT = (1, 0)
LEFT = (-1, 0)
BOTTOM = (0, 1)
TOP = (0, -1)
TOP_LEFT = (-1, -1)
BOTTOM_RIGHT = (1, 1)
TOP_RIGHT = (1, -1)
BOTTOM_LEFT = (-1, 1)


OFFSETS = (RIGHT, LEFT, BOTTOM, TOP, TOP_LEFT, BOTTOM_RIGHT, TOP_RIGHT, BOTTOM_LEFT)
OFFSETS_STRAIGHT = (RIGHT, LEFT, TOP, BOTTOM)


Grid = namedtuple("Grid", "data minX maxX minY maxY")


def print_grid(grid):
    _print_grid(grid.data, grid.maxX, grid.maxY)


def _print_grid(grid, maxX=128, maxY=128, default="."):
    for y in range(maxY):
        r = []
        for x in range(maxX):
            r.append(str(grid.get((x, y), default)))
        print("".join(r))
    print()


def flood_fill(grid, pos, visitor):
    q = [pos]
    visited = set()
    visited.add(pos)

    while len(q) > 0:
        pos = q.pop(0)
        visitor(grid, pos)

        for o in OFFSETS_STRAIGHT:
            neighbour = (pos[0] + o[0], pos[1] + o[1])
            if grid.get(neighbour) == "#" and neighbour not in visited:
                q.append(neighbour)
                visited.add(neighbour)


def get_grid(lines):
    data = {}
    maxX = len(lines[0])
    maxY = len(lines)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            data[(x, y)] = char

    return Grid(data, 0, maxX, 0, maxY)
