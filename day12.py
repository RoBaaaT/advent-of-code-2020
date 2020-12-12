#!/usr/bin/env python3

import sys

def move_dir(x, y, dir, len):
    if dir == 0:
        x += len
    elif dir == 90:
        y += len
    elif dir == 180:
        x -= len
    elif dir == 270:
        y -= len
    else:
        raise RuntimeError('Unexpected dir ' + dir)
    return x, y

def part1(lines):
    x = 0
    y = 0
    dir = 0 # 0 degrees = east (+x)

    for l in lines:
        action = l[0]
        param = int(l[1:])
        if action == 'E':
            x += param
        elif action == 'S':
            y += param
        elif action == 'W':
            x -= param
        elif action == 'N':
            y -= param
        elif action == 'L':
            dir = (360 + dir - param) % 360
        elif action == 'R':
            dir = (dir + param) % 360
        elif action == 'F':
            x, y = move_dir(x, y, dir, param)
        else:
            raise RuntimeError('Unknown action ' + action)

    return x, y, abs(x) + abs(y)



def part2(lines):
    x = 0
    y = 0
    # waypoint position relative to the ship
    rel_x = 10 # 10 east
    rel_y = -1 # 1 north

    for l in lines:
        action = l[0]
        param = int(l[1:])
        if action == 'E':
            rel_x += param
        elif action == 'S':
            rel_y += param
        elif action == 'W':
            rel_x -= param
        elif action == 'N':
            rel_y -= param
        elif action == 'L':
            for i in range(param // 90):
                tmp = rel_x
                rel_x = rel_y
                rel_y = -tmp
        elif action == 'R':
            for i in range(param // 90):
                tmp = rel_x
                rel_x = -rel_y
                rel_y = tmp
        elif action == 'F':
            x += rel_x * param
            y += rel_y * param
        else:
            raise RuntimeError('Unknown action ' + action)

    return x, y, abs(x) + abs(y)

def main(arguments):
    f = open('inputs/day12', 'r')
    lines = f.read().strip('\n').split('\n')

    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))