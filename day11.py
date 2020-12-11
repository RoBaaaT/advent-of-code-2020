#!/usr/bin/env python3

import sys
import math

class Grid:
    def from_input(input):
        lines = input.split('\n')
        height = len(lines)
        width = len(lines[0])
        result = Grid(width, height)
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                result.set(x, y, char)
        return result

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.data = ['.'] * (self.width * self.height)

    def get(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        return self.data[y * self.width + x]

    def set(self, x, y, val):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            raise RuntimeError('x or y out of range')
        self.data[y * self.width + x] = val

    def __str__(self):
        result = ''
        for y in range(self.height):
            for x in range(self.width):
                result += self.get(x, y)
            result += '\n'
        return result

    def __copy__(self):
        result = Grid(self.width, self.height)
        for y in range(self.height):
            for x in range(self.width):
                result.set(x, y, self.get(x, y))
        return result

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.width == self.width and other.height == self.height and other.data == self.data
        else:
            return false

    def occupied_count(self):
        count = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.get(x, y) == '#':
                    count += 1
        return count

def iterate1(grid):
    new_g = Grid(grid.width, grid.height)
    for y in range(grid.height):
        for x in range(grid.width):
            occupied_count = 0
            for y2 in range(y - 1, y + 2):
                for x2 in range(x - 1, x + 2):
                    if y2 != y or x2 != x:
                        val = grid.get(x2, y2)
                        if val == '#':
                            occupied_count += 1
            val = grid.get(x, y)
            if val == 'L' and occupied_count == 0:
                val = '#'
            elif val == '#' and occupied_count >= 4:
                val = 'L'
            new_g.set(x, y, val)
    return new_g

def iterate2(grid):
    new_g = Grid(grid.width, grid.height)
    for y in range(grid.height):
        for x in range(grid.width):
            occupied_count = 0
            for y_dir in range(-1, 2):
                for x_dir in range(-1, 2):
                    if y_dir != 0 or x_dir != 0:
                        offset = 1
                        while True:
                            val = grid.get(x + x_dir * offset, y + y_dir * offset)
                            if val == '#':
                                occupied_count += 1
                                break
                            elif val == None or val == 'L':
                                break
                            offset += 1
            val = grid.get(x, y)
            if val == 'L' and occupied_count == 0:
                val = '#'
            elif val == '#' and occupied_count >= 5:
                val = 'L'
            new_g.set(x, y, val)
    return new_g

def part1(grid):
    prev_g = grid
    while True:
        new_g = iterate1(prev_g)
        if new_g == prev_g:
            return new_g.occupied_count()
        prev_g = new_g
    return -1

def part2(grid):
    prev_g = grid
    while True:
        new_g = iterate2(prev_g)
        if new_g == prev_g:
            return new_g.occupied_count()
        prev_g = new_g
    return -1

def main(arguments):
    f = open('inputs/day11', 'r')
    grid = Grid.from_input(f.read().strip('\n'))

    print(f'Part 1: {part1(grid)}')
    print(f'Part 2: {part2(grid)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))