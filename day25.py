#!/usr/bin/env python3

import sys

def transform(subject, loopsize):
    value = 1
    for _ in range(loopsize):
        value = transform_step(value, subject)
    return value

def transform_step(value, subject):
    value *= subject
    value %= 20201227
    return value

def part1(pubkeys):
    # determine the loop sizes of both pubkeys
    loopsizes = []
    for pubkey in pubkeys:
        val = 1
        loopsize = 0
        while val != pubkey:
            val = transform_step(val, 7)
            loopsize += 1
        loopsizes.append(loopsize)
    # create the encryption keys
    enckeys = [transform(pubkeys[1], loopsizes[0]), transform(pubkeys[0], loopsizes[1])]
    assert(enckeys[0] == enckeys[1])
    return enckeys[0]

def part2(pubkeys):
    return 'Merry christmas!'

def main(arguments):
    f = open('inputs/day25', 'r')
    pubkeys = [int(key) for key in f.read().strip('\n').split('\n')]
    print(f'Part 1: {part1(pubkeys)}')
    print(f'Part 2: {part2(pubkeys)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))