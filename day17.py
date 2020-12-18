#!/usr/bin/env python3

import sys

class Grid:
    def from_input(input):
        lines = input.split('\n')
        height = len(lines)
        width = len(lines[0])
        result = Grid(width, height, 1)
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                result.set(x, y, 0, char)
        return result

    def __init__(self, width, height, depth):
        self.height = height
        self.width = width
        self.depth = depth
        self.data = ['.'] * (self.width * self.height * self.depth)

    def get(self, x, y, z):
        if x < 0 or x >= self.width or y < 0 or y >= self.height or z < 0 or z >= self.depth:
            return None
        return self.data[z * self.width * self.height + y * self.width + x]

    def set(self, x, y, z, val):
        if x < 0 or x >= self.width or y < 0 or y >= self.height or z < 0 or z >= self.depth:
            raise RuntimeError(f'x, y, or z out of range ({x},{y},{z})')
        self.data[z * self.width * self.height + y * self.width + x] = val

    def __str__(self):
        result = ''
        for z in range(self.depth):
            result += f'layer {z}:\n'
            for y in range(self.height):
                for x in range(self.width):
                    val = self.get(x, y, z)
                    result += val if val else ' '
                result += '\n'
        return result

    def occupied_count(self):
        count = 0
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    if self.get(x, y, z) == '#':
                        count += 1
        return count

class Grid4D:
    def from_input(input):
        lines = input.split('\n')
        height = len(lines)
        width = len(lines[0])
        result = Grid4D(width, height, 1, 1)
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                result.set(x, y, 0, 0, char)
        return result

    def __init__(self, width, height, depth, hyper):
        self.height = height
        self.width = width
        self.depth = depth
        self.hyper = hyper
        self.data = ['.'] * (self.width * self.height * self.depth * self.hyper)

    def get(self, x, y, z, w):
        if x < 0 or x >= self.width or y < 0 or y >= self.height or z < 0 or z >= self.depth or w < 0 or w >= self.hyper:
            return None
        return self.data[w * self.depth * self.width * self.height + z * self.width * self.height + y * self.width + x]

    def set(self, x, y, z, w, val):
        if x < 0 or x >= self.width or y < 0 or y >= self.height or z < 0 or z >= self.depth or w < 0 or w >= self.hyper:
            raise RuntimeError(f'x, y, z, or w out of range ({x},{y},{z},{w})')
        self.data[w * self.depth * self.width * self.height + z * self.width * self.height + y * self.width + x] = val

    def occupied_count(self):
        count = 0
        for w in range(self.hyper):
            for z in range(self.depth):
                for y in range(self.height):
                    for x in range(self.width):
                        if self.get(x, y, z, w) == '#':
                            count += 1
        return count

def iterate(grid):
    new_g = Grid(grid.width + 2, grid.height + 2, grid.depth + 2)
    for z in range(grid.depth + 2):
        for y in range(grid.height + 2):
            for x in range(grid.width + 2):
                occupied_count = 0
                for z2 in range(z - 1, z + 2):
                    for y2 in range(y - 1, y + 2):
                        for x2 in range(x - 1, x + 2):
                            if z2 != z or y2 != y or x2 != x:
                                val = grid.get(x2 - 1, y2 - 1, z2 - 1)
                                if val == '#':
                                    occupied_count += 1
                val = grid.get(x - 1, y - 1, z - 1)
                if occupied_count != 2 and occupied_count != 3:
                    val = '.'
                elif occupied_count == 3:
                    val = '#'
                new_g.set(x, y, z, val)
    return new_g

def iterate4D(grid):
    new_g = Grid4D(grid.width + 2, grid.height + 2, grid.depth + 2, grid.hyper + 2)
    for w in range(grid.hyper + 2):
        for z in range(grid.depth + 2):
            for y in range(grid.height + 2):
                for x in range(grid.width + 2):
                    occupied_count = 0
                    for w2 in range(w - 1, w + 2):
                        for z2 in range(z - 1, z + 2):
                            for y2 in range(y - 1, y + 2):
                                for x2 in range(x - 1, x + 2):
                                    if w2 != w or z2 != z or y2 != y or x2 != x:
                                        val = grid.get(x2 - 1, y2 - 1, z2 - 1, w2 - 1)
                                        if val == '#':
                                            occupied_count += 1
                    val = grid.get(x - 1, y - 1, z - 1, w - 1)
                    if occupied_count != 2 and occupied_count != 3:
                        val = '.'
                    elif occupied_count == 3:
                        val = '#'
                    new_g.set(x, y, z, w, val)
    return new_g

def part1(grid):
    for i in range(6):
        grid = iterate(grid)
    return grid.occupied_count()

def part2(grid):
    for i in range(6):
        grid = iterate4D(grid)
    return grid.occupied_count()

def main(arguments):
    f = open('inputs/day17', 'r')
    grid = Grid.from_input(f.read().strip('\n'))
    f.seek(0)
    grid4D = Grid4D.from_input(f.read().strip('\n'))

    print(f'Part 1: {part1(grid)}')
    print(f'Part 2: {part2(grid4D)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))