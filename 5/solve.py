#!/usr/bin/env python3

import hashlib
import sys


def hash(msg):
    m = hashlib.md5()
    m.update(msg.encode('utf-8'))
    return m.hexdigest()


def test():
    assert '1' == hash('abc' + '3231929')[5]
    assert '8' == hash('abc' + '5017308')[5]


def main():
    test()

    secret = 'reyedfim'
    i = 1
    found = 0
    
    indices = set()
    part2 = [0] * 8

    while len(indices) < 8:
        h = hash(secret+str(i))
        if h[:5] == '00000':
            if found < 8:
                print(h[5], end='')
                found += 1

            try:
                idx = int(h[5])

                if -1 < idx < 8 and idx not in indices:
                    part2[idx] = h[6]
                    indices.add(idx)
            except Exception:
                pass

        i += 1

    print()
    print(''.join(part2))


if __name__ == '__main__':
    sys.exit(main())
