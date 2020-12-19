#!/usr/bin/env python3

import sys

class Rule:
    def __init__(self, val):
        self.options = [[int(nt) for nt in opt.split(' ')] for opt in val.split(' | ')]

    def __repr__(self):
        result = ''
        for i, opt in enumerate(self.options):
            for j, nt in enumerate(opt):
                result += str(nt)
                if j + 1 != len(opt):
                    result += ' '
            if i + 1 != len(self.options):
                result += ' | '
        return result

    def matches(self, val, rules):
        for opt in self.options:
            match = True
            off = 0
            for nt in opt:
                matches, length = rules[nt].matches(val[off:], rules)
                if not matches:
                    match = False
                    break
                off += length
            if match:
                return True, off
        return False, 0

    def matches_full(self, val, rules):
        matches, length = self.matches(val, rules)
        return matches and length == len(val)

class Rule0Part2:
    def matches(self, val, rules):
        rule42matches = 0
        off = 0
        while off < len(val):
            matches, length = rules[42].matches(val[off:], rules)
            if not matches:
                break
            off += length
            rule42matches += 1
        if rule42matches == 0:
            return False, 0
        rule31matches = 0
        while off < len(val):
            matches, length = rules[31].matches(val[off:], rules)
            if not matches:
                break
            off += length
            rule31matches += 1
        if rule31matches < rule42matches and rule31matches >= 1:
            return True, off
        return False, 0

    def matches_full(self, val, rules):
        matches, length = self.matches(val, rules)
        return matches and length == len(val)

class Terminal:
    def __init__(self, val):
        self.terminal = val

    def __repr__(self):
        return self.terminal

    def matches(self, val, rules):
        if val.startswith(self.terminal):
            return True, len(self.terminal)
        else:
            return False, 0

def part1(rules, messages):
    return sum([rules[0].matches_full(message, rules) for message in messages])

def part2(rules, messages):
    rules[0] = Rule0Part2()
    return sum([rules[0].matches_full(message, rules) for message in messages])

def main(arguments):
    f = open('inputs/day19', 'r')
    rules, messages = f.read().strip('\n').split('\n\n')
    rules = [rule.split(': ') for rule in rules.split('\n')]
    rules = { int(l): Terminal(r[1:-1]) if r[0] == '"' else Rule(r) for l, r in rules }
    messages = messages.split('\n')
    print(f'Part 1: {part1(rules, messages)}')
    print(f'Part 2: {part2(rules, messages)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))