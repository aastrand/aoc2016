#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


class CPU:
    def __init__(self):
        self.regs = {}
        self.pc = 0

    def _value(self, v):
        try:
            v = int(v)
        except ValueError:
            pass

        return v if isinstance(v, int) else self.regs.get(v, 0)

    def cpy(self, y, x):
        self.regs[x] = self._value(y)
        self.pc += 1

    def inc(self, x, y):
        self.regs[x] = self.regs.get(x, 0) + 1
        self.pc += 1

    def dec(self, x, y):
        self.regs[x] = self.regs.get(x, 0) - 1
        self.pc += 1

    def jnz(self, x, y):
        if self._value(x) != 0:
            self.pc += self._value(y)
        else:
            self.pc += 1


def decode(line):
    parts = line.split(" ")
    instr = parts[0]
    x = parts[1]
    y = 0
    if len(parts) > 2:
        y = parts[2]

    return (instr, x, y)


def part1(filename):
    lines = io.get_lines(filename)

    cpu = CPU()
    while True:
        if cpu.pc > len(lines) - 1:
            break

        instr, x, y = decode(lines[cpu.pc])
        r = getattr(cpu, instr)(x, y)

    return cpu.regs["a"]


def part2(filename):
    lines = io.get_lines(filename)

    cpu = CPU()
    cpu.regs["c"] = 1
    while True:
        if cpu.pc > len(lines) - 1:
            break

        instr, x, y = decode(lines[cpu.pc])
        r = getattr(cpu, instr)(x, y)

    return cpu.regs["a"]


def main():
    assert part1("example.txt") == 42
    print(part1("../input/2016/.txt"))
    print(part2("../input/2016/.txt"))


if __name__ == "__main__":
    sys.exit(main())
