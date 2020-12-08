#!/usr/bin/env python3

import sys

def part1(instructions):
    ip = 0
    acc = 0
    visited_ips = []
    terminated = True
    while True:
        visited_ips.append(ip)
        ins = instructions[ip]['ins']
        arg = instructions[ip]['arg']
        if ins == 'acc':
            acc += arg
            ip += 1
        elif ins == 'jmp':
            ip += arg
        elif ins == 'nop':
            ip += 1

        if ip in visited_ips:
            terminated = False
            break
        if ip >= len(instructions):
            break

    return terminated, acc

def part2(instructions):
    for i, instruction in enumerate(instructions):
        original = instruction['ins']
        replacement = None
        if original == 'nop':
            replacement = 'jmp'
        elif original == 'jmp':
            replacement = 'nop'
        if replacement:
            instructions[i]['ins'] = replacement
            terminated, acc = part1(instructions)
            if terminated:
                return acc
            instructions[i]['ins'] = original
    return -1

def main(arguments):
    f = open('inputs/day8', 'r')
    instructions = [{ 'ins': (s := i.split(' '))[0], 'arg': int(s[1]) } for i in f.read().strip('\n').split('\n')]

    print(f'Part 1: {part1(instructions)}')
    print(f'Part 2: {part2(instructions)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))