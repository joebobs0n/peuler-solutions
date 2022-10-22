#!/usr/bin/python3

import argparse
import time
from functools import reduce
from datetime import timedelta
from typing import *
from pathlib import Path


class Format:
    END =       '\033[0m'
    BOLD =      '\033[1m'
    INVERT =    '\033[3m'
    UNDERLINE = '\033[4m'
    DARKCYAN =  '\033[36m'
    GRAY =      '\033[90m'
    RED =       '\033[91m'
    GREEN =     '\033[92m'
    YELLOW =    '\033[93m'
    BLUE =      '\033[94m'
    PURPLE =    '\033[95m'
    CYAN =      '\033[96m'


def info(msg, sep='\n'):
    print('{}-I-{} {}[ {} ]{} {}'.format(
        Format.GREEN, Format.END,
        Format.GRAY, Path(__file__).stem, Format.END,
        msg
    ), end=sep, flush=True)

def warning(msg):
    print('{}-W-{} {}[ {} ]{} {}'.format(
        Format.YELLOW, Format.END,
        Format.GRAY, Path(__file__).stem, Format.END,
        msg
    ))

def fatal(msg, err_code=1):
    print('{}-F-{} {}[ {} ]{} {}'.format(
        Format.RED, Format.END,
        Format.GRAY, Path(__file__).stem, Format.END,
        msg
    ))
    exit(err_code)

def debug(msg):
    if args.verbose:
        print('{}-V-{} {}'.format(
            Format.PURPLE, Format.END,
            msg
        ))

def helpFormatter(formatter, w=120, h=36):
    try:
        kwargs = {'width': w, 'max_help_position': h}
        formatter(None, **kwargs)
        return lambda prog: formatter(prog, **kwargs)
    except TypeError:
        return formatter

def getArgs():
    ap = argparse.ArgumentParser(
        add_help=False,
        formatter_class=helpFormatter(argparse.MetavarTypeHelpFormatter)
    )
    ap.description = f'\033[1m{page}\033[0m:  {problem}'

    args = ap.add_argument_group('Arguments')
    args.add_argument('-m', '--highestmultiple', type=int, default=20, help='Biggest consecutive multiple for number. Default=20')

    flgs = ap.add_argument_group('Flags')
    flgs.add_argument('-v', '--verbose', action='store_true', default=False, help='Verbose mode -> print debug messages')
    flgs.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit.')

    return ap.parse_args()


def factorize(val):
    x, y = 2, int(val/2)
    while x <= y:
        y = val/x
        if y%1 == 0:
            return (factorize(y) + [x])
        else:
            x += 1
    return [int(val)]

def solve(args):
    solution = []
    factors = []
    for ii in range(1, args.highestmultiple+1):
        factors.append(factorize(ii))
    debug(f'factors of 1-N: {factors}')
    for i in reversed(factors):
        for j in set(i):
            if solution.count(j) < i.count(j):
                solution.extend([j]*(i.count(j) - solution.count(j)))
    debug(f'smallest set of factors: {sorted(solution)}')
    return reduce(lambda x,y: x*y, solution)

if __name__ == '__main__':
    page = 'https://projecteuler.net/problem=5'
    problem = '2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'
    args = getArgs()
    tic = time.time(); solution = solve(args); toc = time.time()
    if args.verbose: print()
    print(f'[{timedelta(seconds=toc-tic)}] \033[1m\033[92manswer\033[0m: {solution}')
