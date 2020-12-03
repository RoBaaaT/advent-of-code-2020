#!/usr/bin/env python3

import sys

def part1(map, slope_x = 3, slope_y = 1):
    count = 0
    x_offset = 0
    y_count = -1
    for row in map:
        y_count += 1
        if y_count % slope_y != 0:
            continue
        if row[x_offset % len(row)] == '#':
            count += 1
        x_offset += slope_x
    return count

def part2(map):
    r1d1 = part1(map, 1, 1)
    r3d1 = part1(map, 3, 1)
    r5d1 = part1(map, 5, 1)
    r7d1 = part1(map, 7, 1)
    r1d2 = part1(map, 1, 2)
    return r1d1 * r3d1 * r5d1 * r7d1 * r1d2

def main(arguments):
    f = open('inputs/day3', 'r')
    map = [l.strip('\n') for l in f.readlines()]
    print(f'Part 1: {part1(map)}')
    print(f'Part 2: {part2(map)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))