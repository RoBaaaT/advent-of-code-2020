#!/usr/bin/env python3

import sys

def part1(rules):
    # create a private copy as we are going to modify rules
    rules = rules.copy()
    count = 0
    search = [ 'shiny gold' ]
    l = []
    while True:
        new_search = []
        for color, contents in rules.items():
            for s in search:
                if s in contents:
                    new_search.append(color)
                    l.append(color)
                    count += 1
                    break
        if len(new_search) == 0:
            break
        for color in new_search:
            rules.pop(color, None)
        search = new_search
    return count

def count_contents(color, rules):
    count = 0
    for color, c in rules[color].items():
        count += c * (1 + count_contents(color, rules))
    return count

def part2(rules):
    return count_contents('shiny gold', rules)

def main(arguments):
    f = open('inputs/day7', 'r')

    rules = {}
    for rule in f.read().split('\n'):
        if len(rule) == 0:
            continue
        bag, contents = rule.split('contain ')
        bag = bag.split(' bags ')[0]
        contents = contents.strip('.')
        c = {}
        if contents != 'no other bags':
            for content in contents.split(', '):
                num, color = content.split(' ', 1)
                num = int(num)
                color = color.split(' bag')[0]
                c[color] = num
        rules[bag] = c
    print(f'Part 1: {part1(rules)}')
    print(f'Part 2: {part2(rules)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))