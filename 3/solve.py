#!/usr/bin/env python3

import sys


def parse(f):
    ls = []
    for l in open(f, 'r'):
        ls.append([int(t.strip()) for t in l.strip().split(' ') if len(t) > 0])

    return ls


def count_real(tris):
    real = 0
    for tri in tris:
        if tri[0]+tri[1] > tri[2] and tri[0]+tri[2] > tri[1] and tri[1]+tri[2] > tri[0]:
            real += 1
    return real


def main(f):
    tris = parse(f)

    print(count_real(tris))

    column_wise = []
    tmp = [[], [], []]
    for n, tri in enumerate(tris, start=1):
        tmp[0].append(tri[0])
        tmp[1].append(tri[1])
        tmp[2].append(tri[2])

        if n % 3 == 0:
            column_wise.append(tmp[0])
            column_wise.append(tmp[1])
            column_wise.append(tmp[2])
            tmp = [[], [], []]

    print(count_real(column_wise))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
