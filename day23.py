#!/usr/bin/env python3

import sys
import time

class Node:
    def __init__(self, data, next, prev_numeric):
        self.data = data
        self.next = next
        self.prev_numeric = prev_numeric

class CLLIterator:
    def __init__(self, cll):
        self.cll = cll
        self.node = cll.head
        self.start = cll.head
        self.first_iter = True

    def __next__(self):
        if not self.first_iter and self.node == self.start:
            raise StopIteration()
        self.first_iter = False
        result = self.node.data
        self.node = self.node.next
        return result

class CircularLinkedList:
    def __init__(self, list):
        self.head = None
        self.tail = None
        self.len = len(list)
        nodes = [None] * len(list)
        prev_node = None
        for i, e in enumerate(list):
            nodes[e - 1] = Node(e, self.head, None)
            if i == 0:
                self.head = nodes[e - 1]
            self.tail = nodes[e - 1]
            if prev_node:
                prev_node.next = nodes[e - 1]
            prev_node = nodes[e - 1]
        nodes[0].prev_numeric = nodes[-1]
        self.head_numeric = nodes[0]
        self.tail_numeric = nodes[-1]
        for i in range(1, len(nodes)):
            nodes[i].prev_numeric = nodes[i - 1]

    def __len__(self):
        return self.len

    def append(self, val):
        if not self.tail:
            raise RuntimeError('Invalid append')
        else:
            # note: the following assumes that the new value is also the new maximum one
            node = Node(val, self.head, None)
            self.tail.next = node
            if self.tail.data == val - 1:
                node.prev_numeric = self.tail
            else:
                prev_num = self.head
                while prev_num.data != val - 1:
                    prev_num = prev_num.next
                    if prev_num == self.head:
                        raise RuntimeError(f'Could not find prev_numeric for {val}')
                node.prev_numeric = prev_num
            self.tail = node
            self.head_numeric.prev_numeric = node
            self.tail_numeric = node
            self.len += 1

    def __iter__(self):
        return CLLIterator(self)



def move(cups, current, max_label):
    sel = current.next
    current.next = sel.next.next.next
    destination = current.prev_numeric
    while True:
        if destination not in [sel, sel.next, sel.next.next]:
            prev_next = destination.next
            destination.next = sel
            sel.next.next.next = prev_next
            break
        destination = destination.prev_numeric
    return current.next

def part1(cups):
    max_label = max(cups)
    cups = CircularLinkedList(cups)
    current = cups.head
    for i in range(100):
        current = move(cups, current, max_label)
    cups = list(cups)
    i = cups.index(1)
    pre1 = cups[0:i]
    cups = cups[i+1:]
    cups.extend(pre1)
    return ''.join(map(lambda c: str(c), cups))

def part2(cups):
    max_label = max(cups)
    cups = CircularLinkedList(cups)
    while len(cups) != 1000000:
        cups.append(max_label + 1)
        max_label += 1

    begin = time.perf_counter()
    current = cups.head
    for i in range(10000000):
        current = move(cups, current, max_label)
    end = time.perf_counter()
    print(f'Elapsed time (part 2): {end - begin:0.4f} seconds')
    cups = list(cups)
    i = cups.index(1)
    cw1 = cups[(i + 1) % len(cups)]
    cw2 = cups[(i + 2) % len(cups)]
    return cw1 * cw2

def main(arguments):
    f = open('inputs/day23', 'r')
    cups = [int(cup) for cup in f.read().strip('\n')]
    print(f'Part 1: {part1(cups.copy())}')
    print(f'Part 2: {part2(cups.copy())}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))