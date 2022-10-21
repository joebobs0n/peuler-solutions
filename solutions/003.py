#!/usr/bin/python3

import argparse
import time
from datetime import timedelta


def debug(msg):
    if args.verbose:
        print(f'\033[2m-V-\033[0m {msg}')

def wide_help_formatter(formatter, w=120, h=36):
    try:
        kwargs = {'width': w, 'max_help_position': h}
        formatter(None, **kwargs)
        return lambda prog: formatter(prog, **kwargs)
    except TypeError:
        return formatter

def getArgs():
    ap = argparse.ArgumentParser(
        add_help=False,
        formatter_class=wide_help_formatter(argparse.MetavarTypeHelpFormatter)
    )
    ap.description = f'\033[1m{page}\033[0m:\n{problem}'

    args = ap.add_argument_group('Arguments')
    args.add_argument('-t', '--target', default=600851475143, type=int, help='Target value for calculation. Default=600851475143')

    flgs = ap.add_argument_group('Flags')
    flgs.add_argument('-v', '--verbose', action='store_true', default=False, help='Verbose mode -> print debug messages')
    flgs.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit.')

    return ap.parse_args()

def factorize(val):
    x, y = 2, int(val/2)
    while x <= y:
        y = val/x
        if y%1 == 0:
            debug(f'x: {x} | y: {y}')
            return (factorize(y) + [x])
        else:
            x += 1
    return [int(val)]

def solve(args):
    return max(factorize(args.target))

if __name__ == '__main__':
    page = 'https://projecteuler.net/problem=3}'
    problem = 'The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?'
    args = getArgs()
    tic = time.time(); solution = solve(args); toc = time.time()
    print(f'\033[1mPrompt\033[0m: {problem}')
    print(f'[{timedelta(seconds=toc-tic)}] \033[1m\033[92manswer\033[0m: {solution}')
