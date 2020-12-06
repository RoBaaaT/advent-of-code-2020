#!/usr/bin/env python3

import sys

def part1(groups):
    count = 0
    for group in groups:
        questions = [False] * 26
        for person in group:
            for answer in person:
                id = ord(answer) - ord('a')
                questions[id] = True
        for question in questions:
            if question:
                count += 1
    return count

def part2(groups):
    count = 0
    for group in groups:
        questions = [[False] * len(group) for _ in [0] * 26]
        for i, person in enumerate(group):
            for answer in person:
                id = ord(answer) - ord('a')
                questions[id][i] = True
        for question in questions:
            if all(question):
                count += 1
    return count

def main(arguments):
    f = open('inputs/day6', 'r')

    groups = [g.strip('\n').split('\n') for g in f.read().split('\n\n')]
    print(f'Part 1: {part1(groups)}')
    print(f'Part 2: {part2(groups)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))