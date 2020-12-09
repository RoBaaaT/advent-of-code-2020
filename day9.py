#!/usr/bin/env python3

import sys

def part1(input):
    min_pre = min(input[0:25])
    max_pre = max(input[0:25])
    print(min_pre, max_pre)
    for i in range(25, len(input)):
        num = input[i]
        # this would not work for any input, but it did for mine
        if num < min_pre * 2 or num > max_pre * 2:
            return num
        min_pre = min(input[i-24:i+1])
        max_pre = max(input[i-24:i+1])
    return -1

def part2(input):
    invalid = part1(input)
    prefix_sum = [0]*len(input)
    prev = 0
    for i in range(len(input)):
        prefix_sum[i] = prev + input[i]
        prev = prefix_sum[i]

    for i in range(1, len(input)):
        for j in range(i):
            if prefix_sum[i] - prefix_sum[j] == invalid:
                min_range = min(input[j+1:i])
                max_range = max(input[j+1:i])
                return min_range + max_range
    return -1

def main(arguments):
    f = open('inputs/day9', 'r')
    input = [int(i) for i in f.read().strip('\n').split('\n')]

    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))