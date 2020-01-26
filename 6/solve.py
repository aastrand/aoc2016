#!/usr/bin/env python3

import sys
from collections import defaultdict


LENGTH = 8


def main(f):
    msg = [0] * LENGTH
    hi = [0] * LENGTH
    freq = [
        defaultdict(int),
        defaultdict(int),
        defaultdict(int),
        defaultdict(int),
        defaultdict(int),
        defaultdict(int),
        defaultdict(int),
        defaultdict(int)
    ]

    for l in open(f, 'r'):
        for i, d in enumerate(l.strip()):
            freq[i][d] += 1

            if freq[i][d] > hi[i]:
                hi[i] = freq[i][d]
                msg[i] = d

    print(''.join(msg))

    for table in freq:
        lo = float('inf')        
        for d, f in table.items():
            if f < lo:
                lo = f
                digit = d
        print(digit, end='')
    print()



if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
