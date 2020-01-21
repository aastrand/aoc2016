#!/usr/bin/env python3

import sys
from collections import defaultdict


def parse(f):
    ls = []
    for l in open(f, 'r'):
        ls.append((l.strip()[:-10], int(l.strip()[-10:-7]), l.strip()[-6:-1]))

    return ls


def checksum(str):
    dict = defaultdict(int)

    for d in str:
        if d != '-':
            dict[d] += 1

    chars = [(k, v * -1) for k, v in dict.items()]
    chars = sorted(chars, key = lambda x: (x[1], x[0]))

    return chars[0][0] + chars[1][0] + chars[2][0] + chars[3][0] + chars[4][0]


# To decrypt a room name, rotate each letter forward through the alphabet a number
# of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A,
# and so on. Dashes become spaces.
def rotate(str, n):
    r = []
    for d in str:
        if d == '-':
            r.append(' ')
        else:
            r.append(chr((((ord(d) - 97) + n) % 26) + 97))

    return ''.join(r[:-1])


def test():
    # aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
    assert 'abxyz' == checksum('aaaaa-bbb-z-y-x-')

    # a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
    assert 'abcde' == checksum('a-b-c-d-e-f-g-h-')

    # not-a-real-room-404[oarel] is a real room.
    assert 'oarel' == checksum('not-a-real-room-')

    # totally-real-room-200[decoy] is not.
    assert 'decoy' != checksum('totally-real-room-')

    # For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.
    assert 'very encrypted name' == rotate('qzmt-zixmtkozy-ivhz-', 343)


def main(f):
    test()

    rooms = parse(f)

    real = 0
    for room in rooms:
        if checksum(room[0]) == room[2]:
            real += room[1]

            if rotate(room[0], room[1]) == 'northpole object storage':
                print(room[1])
    print(real)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
