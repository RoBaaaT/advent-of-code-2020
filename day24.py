#!/usr/bin/env python3

import sys
from enum import Enum

class Direction(Enum):
    E = 1
    W = 2
    SE = 3
    SW = 4
    NW = 5
    NE = 6

    @staticmethod
    def list():
        return list(map(lambda d: d, Direction))

# hex coordinates in "cube" layout (see https://www.redblobgames.com/grids/hexagons/)
class HexCoord:
    def __init__(self, q, r):
        self.q = q
        self.r = r

    def __eq__(self, other):
        return self.q == other.q and self.r == other.r

    def __hash__(self):
        return hash((self.q, self.r))

    def translate(self, dir):
        if dir == Direction.E:
            self.q += 1
        elif dir == Direction.W:
            self.q -= 1
        elif dir == Direction.SE:
            self.r += 1
        elif dir == Direction.NW:
            self.r -= 1
        elif dir == Direction.SW:
            self.q -= 1
            self.r += 1
        elif dir == Direction.NE:
            self.q += 1
            self.r -= 1
        else:
            raise RuntimeError('invalid direction')

    def copy(self):
        return HexCoord(self.q, self.r)

def parse_directions(line):
    result = []
    off = 0
    while off < len(line):
        if line[off] == 'e':
            result.append(Direction.E)
            off += 1
        elif line[off] == 'w':
            result.append(Direction.W)
            off += 1
        elif line[off:off+2] == 'se':
            result.append(Direction.SE)
            off += 2
        elif line[off:off+2] == 'sw':
            result.append(Direction.SW)
            off += 2
        elif line[off:off+2] == 'ne':
            result.append(Direction.NE)
            off += 2
        elif line[off:off+2] == 'nw':
            result.append(Direction.NW)
            off += 2
        else:
            raise RuntimeError('No proper direction found in ' + line[off:])
    return result

def part1(instructions):
    flipped_tiles = {}
    for instruction in instructions:
        coord = HexCoord(0, 0)
        for dir in instruction:
            coord.translate(dir)
        if coord in flipped_tiles:
            flipped_tiles.pop(coord)
        else:
            flipped_tiles[coord] = True
    return flipped_tiles

def part2(flipped_tiles):
    for _ in range(100):
        qs = [coord.q for coord in flipped_tiles.keys()]
        rs = [coord.r for coord in flipped_tiles.keys()]
        min_q = min(qs) - 1 if len(qs) != 0 else -1
        max_q = max(qs) + 1 if len(qs) != 0 else +1
        min_r = min(rs) - 1 if len(rs) != 0 else -1
        max_r = max(rs) + 1 if len(rs) != 0 else +1
        new_flipped_tiles = {}

        for q in range(min_q, max_q + 1):
            for r in range(min_r, max_r + 1):
                coord = HexCoord(q, r)
                adj = 0
                for dir in Direction.list():
                    tcoord = coord.copy()
                    tcoord.translate(dir)
                    if tcoord in flipped_tiles:
                        adj += 1
                if coord in flipped_tiles:
                    if adj == 1 or adj == 2:
                        new_flipped_tiles[coord] = True
                elif adj == 2:
                    new_flipped_tiles[coord] = True

        flipped_tiles = new_flipped_tiles
    return len(flipped_tiles)

def main(arguments):
    f = open('inputs/day24', 'r')
    instructions = [parse_directions(line) for line in f.read().strip('\n').split('\n')]
    flipped_tiles = part1(instructions)
    print(f'Part 1: {len(flipped_tiles)}')
    print(f'Part 2: {part2(flipped_tiles)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))