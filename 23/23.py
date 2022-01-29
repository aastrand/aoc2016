#!/usr/bin/env python3

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from utils import io


class CPU:

    VALID_REGS = set(["a", "b", "c", "d"])

    def __init__(self, code):
        self.regs = {}
        self.pc = 0
        self.code = code

    def _value(self, v):
        try:
            v = int(v)
        except ValueError:
            pass

        return v if isinstance(v, int) else self.regs.get(v, 0)

    def cpy(self, y, x):
        if x in self.VALID_REGS:
            self.regs[x] = self._value(y)
        self.pc += 1

    def inc(self, x, _):
        self.regs[x] = self.regs.get(x, 0) + 1
        self.pc += 1

    def dec(self, x, _):
        self.regs[x] = self.regs.get(x, 0) - 1
        self.pc += 1

    def jnz(self, x, y):
        if self._value(x) != 0:
            self.pc += self._value(y)
        else:
            self.pc += 1

    def tgl(self, x, _):
        offset = self.pc + self._value(x)
        if offset < len(self.code) and offset > -1:
            instr = self.code[offset]

            if instr[2] is None:
                self.code[offset] = (
                    "dec" if instr[0] == "inc" else "inc",
                    instr[1],
                    None,
                )
            elif instr[2] is not None:
                self.code[offset] = (
                    "cpy" if instr[0] == "jnz" else "jnz",
                    instr[1],
                    instr[2],
                )
        self.pc += 1


def decode(line):
    parts = line.split(" ")
    instr = parts[0]
    x = None
    if len(parts) > 1:
        x = parts[1]
    y = None
    if len(parts) > 2:
        y = parts[2]

    return (instr, x, y)


def part1(filename, a=0):
    lines = io.get_lines(filename)
    code = [decode(line) for line in lines]

    cpu = CPU(code)
    cpu.regs["a"] = a
    while True:
        if cpu.pc > len(cpu.code) - 1:
            break

        instr, x, y = cpu.code[cpu.pc]
        r = getattr(cpu, instr)(x, y)

    return cpu.regs["a"]


def part2(filename):
    lines = io.get_lines(filename)
    code = [decode(line) for line in lines]

    cpu = CPU(code)
    cpu.regs["a"] = 12
    while True:
        if cpu.pc > len(cpu.code) - 1:
            break

        if cpu.pc == 5:
            cpu.regs["a"] += cpu.regs.get("b", 0) * cpu.regs.get("d", 0)
            cpu.regs["c"] = 0
            cpu.regs["d"] = 0
            cpu.pc = 10

        instr, x, y = cpu.code[cpu.pc]
        r = getattr(cpu, instr)(x, y)

    return cpu.regs["a"]


def main():
    assert part1("example.txt") == 3
    print(part1("input.txt", 7))

    print(part2("input.txt"))


if __name__ == "__main__":
    sys.exit(main())
