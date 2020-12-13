#!/usr/bin/env python3

import sys
import functools
import operator

def part1(earliest, timestamps):
    earliest_id = -1
    earliest_diff = sys.maxsize
    for id in timestamps:
        if id:
            diff = id - (earliest % id)
            if earliest_diff > diff:
                earliest_diff = diff
                earliest_id = id

    return earliest_id * earliest_diff


def part2(timestamps):
    busses = [(timestamps[i], i) for i in range(len(timestamps))]
    busses = [(bus, (bus - num) % bus) for bus, num in busses if bus]
    product = functools.reduce(operator.mul, [bus for bus, num in busses], 1)
    B = [product // bus for bus, num in busses]
    x = [pow(B[i], -1, busses[i][0]) for i in range(len(B))]
    sum_list = [B[i] * x[i] * busses[i][1] for i in range(len(B))]
    return functools.reduce(operator.add, sum_list, 0) % product

def main(arguments):
    f = open('inputs/day13', 'r')
    earliest, timestamps = f.read().strip('\n').split('\n')
    earliest = int(earliest)
    timestamps = [int(t) if t != 'x' else None for t in timestamps.split(',')]

    print(f'Part 1: {part1(earliest, timestamps)}')
    print(f'Part 2: {part2(timestamps)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))