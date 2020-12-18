#!/usr/bin/env python3

import sys

def apply_op(val, op, operand):
    if op == '+':
        return val + operand
    elif op == '*':
        return val * operand
    else:
        raise RuntimeError(f'Unknown operator "{op}"')

def evaluate_expression(expr):
    result = 0
    o = 0
    op = '+'
    # parse left-to-right
    while (o < len(expr)):
        if expr[o] == ' ':
            o += 1
        elif expr[o] == '(':
            open_count = 0
            for i in range(o + 1, len(expr)):
                if expr[i] == '(':
                    open_count += 1
                elif expr[i] == ')':
                    if open_count > 0:
                        open_count -= 1
                    else: # found closing parenthesis -> evaluate sub-expression recursively
                        result = apply_op(result, op, evaluate_expression(expr[o + 1:i]))
                        o = i + 1
        elif expr[o] == '+' or expr[o] == '*':
            op = expr[o]
            o += 1
        else: # should be an int
            operand = int(expr[o])
            result = apply_op(result, op, operand)
            o += 1

    return result

def evaluate_expression_adv(expr):
    result = 0
    o = 0
    op = '+'
    # parse left-to-right
    while (o < len(expr)):
        if expr[o] == ' ':
            o += 1
        elif expr[o] == '(':
            open_count = 0
            for i in range(o + 1, len(expr)):
                if expr[i] == '(':
                    open_count += 1
                elif expr[i] == ')':
                    if open_count > 0:
                        open_count -= 1
                    else: # found closing parenthesis -> evaluate sub-expression recursively
                        result = apply_op(result, op, evaluate_expression_adv(expr[o + 1:i]))
                        o = i + 1
        elif expr[o] == '+' or expr[o] == '*':
            op = expr[o]
            o += 1
            if op == '*':
                operand = evaluate_expression_adv(expr[o:])
                o = len(expr)
                result = apply_op(result, op, operand)
        else: # should be an int
            operand = int(expr[o])
            o += 1
            result = apply_op(result, op, operand)

    return result

def part1(expressions):
    result = 0
    for expr in expressions:
        result += evaluate_expression(expr)
    return result

def part2(expressions):
    result = 0
    for expr in expressions:
        result += evaluate_expression_adv(expr)
    return result

def main(arguments):
    f = open('inputs/day18', 'r')
    expressions = f.read().strip('\n').split('\n')
    print(f'Part 1: {part1(expressions)}')
    print(f'Part 2: {part2(expressions)}')

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))