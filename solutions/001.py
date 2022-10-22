#!/usr/bin/python3

import argparse
import time
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
    args.add_argument('-t', '--target', type=int, default=1000, help='Target max value. Default=1000')
    args.add_argument('-m', '--multiples', type=int, nargs='*', default=[3,5], help='Multiples to find. Default=[3,5]')

    flgs = ap.add_argument_group('Flags')
    flgs.add_argument('-v', '--verbose', action='store_true', default=False, help='Verbose mode -> print debug messages')
    flgs.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit.')

    return ap.parse_args()


def isDivisible(val: int, multiples: List[int]) -> bool:
    if val != 0:
        for mm in multiples:
            if val%mm == 0: return True
    return False

def solve(args):
    solution = []
    for val in (x for x in range(args.target) if isDivisible(x, args.multiples)):
        solution.append(val)
    debug(solution)
    return sum(solution)

if __name__ == '__main__':
    page = 'https://projecteuler.net/problem=1'
    problem = 'If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.'
    args = getArgs()
    tic = time.time(); solution = solve(args); toc = time.time()
    if args.verbose: print()
    print(f'[{timedelta(seconds=toc-tic)}] \033[1m\033[92manswer\033[0m: {solution}')
