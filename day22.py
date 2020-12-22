#!/usr/bin/env python3

import sys

def part1(player1, player2):
    while len(player1) != 0 and len(player2) != 0:
        p1 = player1.pop(0)
        p2 = player2.pop(0)
        if p1 > p2:
            player1.append(p1)
            player1.append(p2)
        else:
            player2.append(p2)
            player2.append(p1)
    winner = player2 if len(player1) == 0 else player1
    return sum([(i + 1) * val for i, val in enumerate(winner[::-1])])

def determine_winner(p1, p2, player1, player2, level):
    if len(player1) >= p1 and len(player2) >= p2: # recurse
        player1_rec = player1[0:p1].copy()
        player2_rec = player2[0:p2].copy()
        return recursive_combat(player1_rec, player2_rec, level + 1)
    else:
        if p1 > p2:
            return 1
        else:
            return 2
    return -1

def recursive_combat(player1, player2, level = 0):
    prev_rounds = []
    while len(player1) != 0 and len(player2) != 0:
        if [player1, player2] not in prev_rounds:
            prev_rounds.append([player1.copy(), player2.copy()])
            p1 = player1.pop(0)
            p2 = player2.pop(0)
            w = determine_winner(p1, p2, player1, player2, level)
        else:
            return 1
        if w == 1:
            player1.append(p1)
            player1.append(p2)
        elif w == 2:
            player2.append(p2)
            player2.append(p1)
        else:
            raise RuntimeError(f'Unexpected winner: {w}')
    return 1 if len(player2) == 0 else 2

def part2(player1, player2):
    w = recursive_combat(player1, player2)
    winner = player2 if w == 2 else player1
    return sum([(i + 1) * val for i, val in enumerate(winner[::-1])])

def main(arguments):
    f = open('inputs/day22', 'r')
    players = [[int(card) for card in player.split('\n')[1:]] for player in f.read().strip('\n').split('\n\n')]
    print(f'Part 1: {part1(players[0].copy(), players[1].copy())}')
    print(f'Part 2: {part2(players[0].copy(), players[1].copy())}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))