#!/usr/bin/env python3

import os
import sys
from distutils.file_util import move_file
from shutil import move

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


# The first floor contains a promethium generator and a promethium-compatible microchip.
# The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
# The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
# The fourth floor contains nothing relevant.

# F4 .  .   .   .   .   .   .   .   .   .   .
# F3 .  .   .   .   .   .   .   COM CUM RUM PLM
# F2 .  .   .   COG CUG RUG PLG .   .   .   .
# F1 E  PRG PRM .   .   .   .   .   .   .   .

# to move n items up 1 floor, it requires 2 * (n - 1) - 1 moves

# for work "already done", subtract 2n - (n-1) + 1 moves per floor

# 17 + 17 + 17 - 6 - 6 - 6

# you notice some extra parts on the first floor that weren't listed on the record outside:

# An elerium generator.
# An elerium-compatible microchip.
# A dilithium generator.
# A dilithium-compatible microchip.

# F4 .  .   .   .   .   .   .   .   .   .   .   .   .   .   .
# F3 .  .   .   .   .   .   .   COM CUM RUM PLM .   .   .   .
# F2 .  .   .   COG CUG RUG PLG .   .   .   .   .   .   .   .
# F1 E  PRG PRM .   .   .   .   .   .   .   .   EM  EG  DG  DM

# 25 + 25 + 25 - 6 - 6 - 6

# Not a great puzzle, at all


def solve(input):
    total = sum(input)
    move_three_floors = (2 * (total - 1) - 1) * 3
    already_done = 0

    for floor in range(1, 4):
        if input[floor] > 0:
            already_done += ((2 * input[floor]) - (input[floor] - 1) + 1) * floor

    return move_three_floors - already_done


def main():
    print(solve([2, 4, 4, 0]))
    print(solve([6, 4, 4, 0]))


if __name__ == "__main__":
    sys.exit(main())
