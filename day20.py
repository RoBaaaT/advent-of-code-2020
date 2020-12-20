#!/usr/bin/env python3

import sys

class Tile:
    def __init__(self, data):
        self.data = data.split('\n')

    def __repr__(self):
        return '\n'.join(self.data)

    def get_edges(self):
        return [self.data[0], ''.join([line[-1] for line in self.data]), self.data[-1][::-1], ''.join([line[0] for line in self.data[::-1]])]

def part1(tiles):
    result = 1
    for id1, tile1 in tiles.items():
        edges1 = tile1.get_edges()
        num_matches = 0
        for id2, tile2 in tiles.items():
            edges2 = tile2.get_edges()
            if id1 != id2:
                for edge1 in edges1:
                    edge_match = False
                    for edge2 in edges2:
                        if edge1 == edge2 or edge1 == edge2[::-1]:
                            edge_match = True
                            break
                    if edge_match:
                        num_matches += 1
                        break
        if num_matches == 2:
            result *= id1
            print(id1)

    return result

def part2(tiles):
    return -1

def main(arguments):
    f = open('inputs/day20', 'r')
    tiles = f.read().strip('\n').split('\n\n')
    tiles = {int((sp := tile.split('\n', 1))[0].split('Tile ')[1].strip(':')): Tile(sp[1]) for tile in tiles}
    print(f'Part 1: {part1(tiles)}')
    print(f'Part 2: {part2(tiles)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))