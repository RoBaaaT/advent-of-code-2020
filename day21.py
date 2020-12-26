#!/usr/bin/env python3

import sys

def part1(ilist, allergen_possibilities):
    alist = {}
    for i, line in enumerate(ilist):
        for allergen in line[1]:
            if not allergen in alist:
                alist[allergen] = [i]
            else:
                alist[allergen].append(i)
    all_possibilities = []
    for allergen, lines in alist.items():
        possibilities = ilist[lines[0]][0].copy()
        for i in lines[1:]:
            ingredients = ilist[i][0]
            possibilities = [p for p in possibilities if p in ingredients]
        allergen_possibilities[allergen] = possibilities
        all_possibilities.extend([p for p in possibilities if p not in all_possibilities])
    return sum([len([ing for ing in line[0] if ing not in all_possibilities]) for line in ilist])

def part2(ilist, allergen_possibilities):
    unknowns = list(allergen_possibilities.keys())
    while len(unknowns) > 0:
        newly_known = [u for u in unknowns if len(allergen_possibilities[u]) == 1][0]
        unknowns.remove(newly_known)
        known_ing = allergen_possibilities[newly_known][0]
        for allergen in allergen_possibilities:
            if allergen != newly_known:
                if known_ing in allergen_possibilities[allergen]:
                    allergen_possibilities[allergen].remove(known_ing)
    return ','.join([allergen_possibilities[a][0] for a in sorted(allergen_possibilities.keys())])

def main(arguments):
    f = open('inputs/day21', 'r')
    ilist = [((split := line.split(' (contains '))[0].split(' '), split[1][0:-1].split(', ')) for line in f.read().strip('\n').split('\n')]
    allergen_possibilities = {}
    print(f'Part 1: {part1(ilist, allergen_possibilities)}')
    print(f'Part 2: {part2(ilist, allergen_possibilities)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))