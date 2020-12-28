#!/usr/bin/env python3

import sys

class Tile:
    def __init__(self, data):
        self.data = data.split('\n')

    def __repr__(self):
        return '\n'.join(self.data)

    def get_edges(self):
        return [self.data[0], ''.join([line[-1] for line in self.data]), self.data[-1], ''.join([line[0] for line in self.data])]

    def flip_h(self):
        self.data = [line[::-1] for line in self.data]

    def flip_v(self):
        self.data = self.data[::-1]

    def rotate_l(self):
        self.data = [''.join([self.data[x][len(self.data) - y - 1] for x in range(len(self.data[y]))]) for y in range(len(self.data))]

def part1(tiles, img):
    result = 1
    corner_id = -1
    for id1, tile1 in tiles.items():
        edges1 = tile1.get_edges()
        edge_matches = []
        for id2, tile2 in tiles.items():
            if id1 != id2:
                edges2 = tile2.get_edges()
                for i, edge1 in enumerate(edges1):
                    edge_match = False
                    for edge2 in edges2:
                        if edge1 == edge2 or edge1 == edge2[::-1]:
                            edge_match = True
                            break
                    if edge_match:
                        edge_matches.append(i)
                        break
        if len(edge_matches) == 2:
            result *= id1
            if 0 in edge_matches:
                tile1.flip_v()
            if 3 in edge_matches:
                tile1.flip_h()
            # save a corner id to start assembling the image from that point in the next step
            corner_id = id1

    # assemble the image
    curr_x = 1
    curr_y = 0
    # start at the top left corner
    tile_map = [[]]
    tile_map[curr_y].append(tiles.pop(corner_id))

    while (len(tiles) > 0):
        # try to find a tile that fits to the right of the last one
        l_edge = tile_map[curr_y][curr_x - 1].get_edges()[1] if curr_x != 0 else None
        t_edge = tile_map[curr_y - 1][curr_x].get_edges()[2] if curr_y != 0 and len(tile_map[curr_y - 1]) > curr_x else None
        found_tile = False
        for id, tile in tiles.items():
            edges = tile.get_edges()
            match_i = -1
            l_match = None
            for i, edge in enumerate(edges):
                if l_edge and (l_edge == edge or l_edge[::-1] == edge):
                    match_i = i
                    l_match = True
                    break
                elif t_edge and (t_edge == edge or t_edge[::-1] == edge):
                    match_i = i
                    l_match = False
            if match_i == -1:
                continue # try another tile

            match_i = match_i + 4
            if l_match:
                while match_i != 3:
                    match_i -= 1
                    tile.rotate_l()
                if l_edge != tile.get_edges()[3]:
                    tile.flip_v()
            else:
                while match_i != 0:
                    match_i -= 1
                    tile.rotate_l()
                if t_edge != tile.get_edges()[0]:
                    tile.flip_h()

            # check that we have rotated and flipped properly
            if l_edge:
                assert(l_edge == tile.get_edges()[3])
            if t_edge:
                assert(t_edge == tile.get_edges()[0])
            tile_map[curr_y].append(tiles.pop(id))
            curr_x += 1
            found_tile = True
            break
        if not found_tile: # advance to the next row
            curr_x = 0
            curr_y += 1
            tile_map.append([])

    tile_size = len(tile_map[0][0].data) - 2
    map_width = len(tile_map[0])
    map_height = len(tile_map)
    img.extend([[None for _ in range(map_width * tile_size)] for _ in range(map_height * tile_size)])
    for my in range(map_height):
        for mx in range(map_width):
            for tx in range(tile_size):
                for ty in range(tile_size):
                    img[my * tile_size + ty][mx * tile_size + tx] = tile_map[my][mx].data[ty + 1][tx + 1]

    return result

def part2(img):
    pattern = [ "                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   " ]
    pattern_width = len(pattern[0])
    pattern_height = len(pattern)
    img_size = len(img)

    for _ in range(4): # rotate the image up to four times
        for _ in range(2): # look for sea monsters in flipped/unflipped versions of the image
            any_match = False
            for x in range(img_size - pattern_width):
                for y in range(img_size - pattern_height):
                    match = True
                    for px in range(pattern_width):
                        if not match:
                            break
                        for py in range(pattern_height):
                            pval = pattern[py][px]
                            if pval == '#' and img[y + py][x + px] != pval:
                                match = False
                                break
                    if match:
                        any_match = True
                        for px in range(pattern_width):
                            for py in range(pattern_height):
                                pval = pattern[py][px]
                                if pval == '#':
                                    img[y + py][x + px] = 'O'
            if any_match:
                count = 0
                for x in range(img_size):
                    for y in range(img_size):
                        if img[y][x] == '#':
                            count += 1
                return count
            # flip horizontally
            img = [line[::-1] for line in img]
        # rotate
        img = [[img[x][len(img) - y - 1] for x in range(len(img[y]))] for y in range(len(img))]

    return -1

def main(arguments):
    f = open('inputs/day20', 'r')
    tiles = f.read().strip('\n').split('\n\n')
    tiles = {int((sp := tile.split('\n', 1))[0].split('Tile ')[1].strip(':')): Tile(sp[1]) for tile in tiles}
    img = []
    print(f'Part 1: {part1(tiles, img)}')
    # print the image
    #for line in [''.join(line) for line in img]:
    #    print(line)
    print(f'Part 2: {part2(img)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))