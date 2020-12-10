#!/usr/bin/env python3

import sys
import math

def part1(adapters):
    s = sorted(adapters)
    s.insert(0, 0)
    count1 = 0
    count3 = 1 # built-in adapter
    for i in range(1, len(s)):
        diff = s[i] - s[i - 1]
        if diff == 1:
            count1 += 1
        elif diff == 3:
            count3 += 1
        else:
            return "invalid diff " + diff
    return count1 * count3

def binom(n, k):
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))

def part2(adapters):
    s = sorted(adapters)
    s.insert(0, 0)
    s.append(s[-1] + 3)
    print(s)
    fixed_points = []
    fixed_points.append(0) # outlet
    for i in range(0, len(s)):
        if i > 0 and s[i] - s[i - 1] == 3:
            fixed_points.append(i)
        elif i < len(s) - 1 and s[i + 1] - s[i] == 3:
            fixed_points.append(i)

    result = 1
    for i in range(1, len(fixed_points)):
        end = fixed_points[i]
        begin = fixed_points[i - 1]
        diff = s[end] - s[begin]
        # how many adapters do we need in this range at minimum?
        mandatory_count = ((diff + 2) // 3 - 1)
        # how many adapters are in this range if we use all of them?
        max_count = end - begin - 1
        # we can use between mandatory_count and max_count adapters in this range
        possibilities = 1 # there is only one way to arrange max_count adapters in a range that has max_count adapters
        for j in range(mandatory_count, max_count):
            possibilities += binom(max_count, j)
        result *= possibilities
    return result

def main(arguments):
    f = open('inputs/day10', 'r')
    adapters = [int(a) for a in f.read().strip('\n').split('\n')]

    print(f'Part 1: {part1(adapters)}')
    print(f'Part 2: {part2(adapters)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))