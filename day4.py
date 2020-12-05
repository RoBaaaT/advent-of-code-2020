#!/usr/bin/env python3

import sys
import string

def part1(batch):
    count = 0
    for pp in batch:
        if 'byr' in pp and 'iyr' in pp and 'eyr' in pp and 'hgt' in pp and 'hcl' in pp and 'ecl' in pp and 'pid' in pp:
            count += 1
    return count

def part2(batch):
    count = 0
    for pp in batch:
        if 'byr' in pp and 'iyr' in pp and 'eyr' in pp and 'hgt' in pp and 'hcl' in pp and 'ecl' in pp and 'pid' in pp:
            byr = int(pp['byr'])
            if byr < 1920 or byr > 2002:
                continue
            iyr = int(pp['iyr'])
            if iyr < 2010 or iyr > 2020:
                continue
            eyr = int(pp['eyr'])
            if eyr < 2020 or eyr > 2030:
                continue
            hgt = pp['hgt']
            if hgt.endswith('cm'):
                hgt_cm = int(hgt.strip('cm'))
                if hgt_cm < 150 or hgt_cm > 193:
                    continue
            elif hgt.endswith('in'):
                hgt_in = int(hgt.strip('in'))
                if hgt_in < 59 or hgt_in > 76:
                    continue
            else:
                continue
            hcl = pp['hcl']
            if len(hcl) != 7 or hcl[0] != '#' or not all(c in string.hexdigits for c in hcl[1:7]):
                continue
            ecl = pp['ecl']
            if not ecl in [ 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' ]:
                continue
            pid = pp['pid']
            if len(pid) != 9 or not pid.isdecimal():
                continue
            count += 1
    return count


def main(arguments):
    f = open('inputs/day4', 'r')
    input = [l.strip('\n') for l in f.readlines()]
    batch = []
    current = {}
    for line in input:
        if not line:
            batch.append(current)
            current = {}
            continue
        for kv in line.split(' '):
            key, value = kv.split(':')
            current[key] = value
    batch.append(current)

    print(f'Part 1: {part1(batch)}')
    print(f'Part 2: {part2(batch)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
