#!/usr/bin/env python3

import sys

def part1(passes):
    return max(passes, key=lambda p: p['id'])

def part2(passes):
    passes = sorted(passes, key=lambda p: p['id'])
    prev = passes[0]['id']
    for i in range(1, len(passes)):
        id = passes[i]['id']
        if id != prev + 1:
            return prev + 1
        prev = id

def main(arguments):
    f = open('inputs/day5', 'r')
    raw_passes = [l.strip('\n') for l in f.readlines()]
    passes = []
    for raw_pass in raw_passes:
        h = 127
        l = 0
        for i in range(7):
            m = l + (h - l) // 2
            if raw_pass[i] == 'F':
                h = m
            elif raw_pass[i] == 'B':
                l = m + 1
        row = l
        l = 0
        r = 7
        for i in range(3):
            m = l + (r - l) // 2
            if raw_pass[7 + i] == 'L':
                r = m
            elif raw_pass[7 + i] == 'R':
                l = m + 1
        col = l
        id = row * 8 + l
        passes.append({
            'raw': raw_pass,
            'row': row,
            'col': col,
            'id': id
        })

    print(f'Part 1: {part1(passes)}')
    print(f'Part 2: {part2(passes)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))