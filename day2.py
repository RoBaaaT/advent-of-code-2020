#!/usr/bin/env python3

import os
import sys

def part1(list):
    valid_count = 0
    for policy, password in list:
        counts, char = policy.split(' ')
        min, max = counts.split('-')
        min = int(min)
        max = int(max)
        char_count = 0
        for c in password:
            if c == char:
                char_count += 1
        if char_count >= min and char_count <= max:
            valid_count += 1
    return valid_count

def part2(list):
    valid_count = 0
    for policy, password in list:
        counts, char = policy.split(' ')
        pos1, pos2 = counts.split('-')
        pos1 = int(pos1)
        pos2 = int(pos2)
        if (password[pos1] == char) ^ (password[pos2] == char):
            valid_count += 1
    return valid_count

def main(arguments):
    f = open('inputs/day2', 'r')
    list = [l.strip('\n').split(':') for l in f.readlines()]
    print(f'Part 1: {part1(list)}')
    print(f'Part 2: {part2(list)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))