#!/usr/bin/env python3

import sys

def part1(rules, nearby):
    tser = 0
    new_nearby = []
    for ticket in nearby:
        ticket_valid = True
        for val in ticket:
            valid = False
            for rule in rules.values():
                if (val >= rule[0][0] and val <= rule[0][1]) or (val >= rule[1][0] and val <= rule[1][1]):
                    valid = True
                    break
            if not valid:
                tser += val
                ticket_valid = False
        if ticket_valid:
            new_nearby.append(ticket)
    nearby.clear()
    nearby.extend(new_nearby)
    return tser

def part2(rules, my, nearby):
    field_count = len(my)
    all_tickets = nearby.copy()
    all_tickets.append(my)

    # determine for all fields at which positions they COULD be based on the fact that no value would be invalid
    possible_positions = {}
    for field, rule in rules.items():
        possible_positions[field] = []
        for i in range(field_count):
            valid = True
            for ticket in all_tickets:
                val = ticket[i]
                if (val < rule[0][0] or val > rule[0][1]) and (val < rule[1][0] or val > rule[1][1]):
                    valid = False
                    break
            if valid:
                possible_positions[field].append(i)

    # based on the possible positions for each individual field, find an order that puts each field on one of its possible positions
    positions = { i: [] for i in range(field_count) }
    for field, poss in possible_positions.items():
        for pos in poss:
            positions[pos].append(field)
    undecided_positions = [i for i in range(field_count)]
    while len(undecided_positions) > 0:
        newly_decided = -1
        for pos in undecided_positions:
            if len(positions[pos]) == 1:
                newly_decided = pos
                field = positions[pos][0]
                positions[pos] = field
                for p in undecided_positions:
                    if p != pos:
                        positions[p].remove(field)
                break
        if newly_decided != -1:
            undecided_positions.remove(newly_decided)
        else:
            raise RuntimeError('Could not decide the positions of all fields!')

    # calculate the product of the six 'departure' fields on my ticket
    result = 1
    for i in range(field_count):
        if positions[i].startswith('departure'):
            result *= my[i]

    return result

def main(arguments):
    f = open('inputs/day16', 'r')
    rules, my, nearby = f.read().strip('\n').split('\n\n')
    rules = { (split:=line.split(': '))[0]: [[int(val) for val in rnge.split('-')] for rnge in split[1].split(' or ')] for line in rules.split('\n') }
    my = [int(val) for val in my.split('\n')[1].split(',')]
    nearby = [[int(val) for val in line.split(',')] for line in nearby.split('\n')[1:]]

    print(f'Part 1: {part1(rules, nearby)}')
    print(f'Part 2: {part2(rules, my, nearby)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))