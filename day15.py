#!/usr/bin/env python3

import sys

def part1(numbers):
    numbers = numbers.copy()
    count = len(numbers)
    while count != 2020:
        last = numbers[-1]
        new = 0
        for i in range(len(numbers) - 1):
            if numbers[-2 - i] == last:
                new = i + 1
                break
        numbers.append(new)
        count += 1
    return numbers[-1]

def part2(numbers):
    last_pos = {}
    count = len(numbers)
    for i, num in enumerate(numbers[0:-1]):
        last_pos[num] = i
    last = numbers[-1]
    while count != 30000000:
        new = 0
        if last in last_pos:
            new = count - last_pos[last] - 1
        last_pos[last] = count - 1
        last = new
        count += 1
    return last

def main(arguments):
    f = open('inputs/day15', 'r')
    numbers = [int(n) for n in f.read().strip('\n').split(',')]

    print(f'Part 1: {part1(numbers)}')
    print(f'Part 2: {part2(numbers)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))