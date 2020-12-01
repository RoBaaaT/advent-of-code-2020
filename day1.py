#!/usr/bin/env python3

import os
import sys

def part1(expenses):
    for i in range(len(expenses)):
        val = expenses[i]
        search_val = 2020 - val
        for j in range(i + 1, len(expenses)):
            if expenses[j] == search_val:
                return val * search_val
    return 0

def part2(expenses):
    expenses.sort()
    for i in range(len(expenses)):
        val1 = expenses[i]
        for j in range(i + 1, len(expenses)):
            val2 = expenses[j]
            search_val = 2020 - val1 - val2
            if search_val <= 0:
                break
            for k in range(j + 1, len(expenses)):
                if expenses[k] == search_val:
                    return val1 * val2 * search_val
                elif expenses[k] > search_val:
                    break
    return expenses

def main(arguments):
    f = open('inputs/day1', 'r')
    expenses = [int(l) for l in f.readlines()]

    print(f'Part 1: {part1(expenses)}')
    print(f'Part 2: {part2(expenses)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))