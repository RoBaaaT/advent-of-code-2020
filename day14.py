#!/usr/bin/env python3

import sys
import functools
import operator

class MaskSet:
    def __init__(self, mask):
        self.mask = mask

    def __repr__(self):
        return f'MaskSet({self.mask})'

class MemSet:
    def __init__(self, addr, val):
        self.addr = addr
        self.val = val

    def __repr__(self):
        return f'MemSet({self.addr},{self.val})'

def part1(instructions):
    mask = 'X' * 36
    mem = {}
    for instruction in instructions:
        if isinstance(instruction, MaskSet):
            mask = instruction.mask
        elif isinstance(instruction, MemSet):
            val = instruction.val
            for i in range(36):
                if mask[i] == '0':
                    val &= ~(1 << (35 - i))
                elif mask[i] == '1':
                    val |= 1 << (35 - i)
            mem[instruction.addr] = val
    return sum(mem.values())

def set_mem(mem, addr, floating, val):
    if len(floating) > 0:
        set_mem(mem, addr | (1 << floating[0]), floating[1:], val)
        set_mem(mem, addr & ~(1 << floating[0]), floating[1:], val)
    else:
        mem[addr] = val

def part2(instructions):
    mask = 'X' * 36
    mem = {}
    for instruction in instructions:
        if isinstance(instruction, MaskSet):
            mask = instruction.mask
        elif isinstance(instruction, MemSet):
            val = instruction.val
            addr = instruction.addr
            floating = []
            for i in range(36):
                if mask[i] == 'X':
                    floating.append(35 - i)
                elif mask[i] == '1':
                    addr |= 1 << (35 - i)
            set_mem(mem, addr, floating, val)
    return sum(mem.values())

def main(arguments):
    f = open('inputs/day14', 'r')
    lines = f.read().strip('\n').split('\n')
    instructions = []
    for line in lines:
        l, r = line.split(' = ')
        if l == "mask":
            instructions.append(MaskSet(r))
        elif l.startswith('mem['):
            addr = int(l[4:].strip(']'))
            val = int(r)
            instructions.append(MemSet(addr, val))
        else:
            raise RuntimeError(f'Unexpected instruction "{line}"')

    print(f'Part 1: {part1(instructions)}')
    print(f'Part 2: {part2(instructions)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))