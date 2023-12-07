#!/usr/bin/env python3

import os
import sys
from collections import defaultdict, namedtuple

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io
from utils.parse import ints

Give = namedtuple("give", "sender low_type low_to high_type high_to")


def solve(filename, cmp1, cmp2):
    lines = io.get_lines(filename)

    bots = defaultdict(list)
    gives = {}
    val_count = 0
    for line in lines:
        nums = ints(line)

        if "value" in line:
            bots[nums[1]].append(nums[0])
            val_count += 1
        elif "gives" in line:
            low_type = "output" if "low to output" in line else "bot"
            high_type = "output" if "high to output" in line else "bot"
            gives[nums[0]] = Give(nums[0], low_type, nums[1], high_type, nums[2])

            if low_type == "bot":
                if nums[1] not in bots:
                    bots[nums[1]] = []
            if high_type == "bot":
                if nums[2] not in bots:
                    bots[nums[2]] = []

    output = {}
    part1_bot = None

    while len(output.keys()) != val_count:
        for bot, nums in bots.items():
            if len(nums) == 2:
                low = min(bots[bot])
                high = max(bots[bot])

                if (low, high) == (cmp1, cmp2) or (high, low) == (cmp1, cmp2):
                    part1_bot = bot

                if gives[bot].low_type == "bot":
                    bots[gives[bot].low_to].append(low)
                else:
                    output[gives[bot].low_to] = low

                if gives[bot].high_type == "bot":
                    bots[gives[bot].high_to].append(high)
                else:
                    output[gives[bot].high_to] = high

                bots[bot] = []

    return part1_bot, output[0] * output[1] * output[2]


def main():
    assert solve("example.txt", 5, 2)[0] == 2
    r = solve("../input/2016/.txt", 61, 17)
    print(r[0])
    print(r[1])


if __name__ == "__main__":
    sys.exit(main())
