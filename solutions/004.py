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
    args.add_argument('test', type=int)

    flgs = ap.add_argument_group('Flags')
    flgs.add_argument('-v', '--verbose', action='store_true', default=False, help='Verbose mode -> print debug messages')
    flgs.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit.')

    return ap.parse_args()


def isPalindrome(num: int) -> bool:
    num = str(num)
    debug(num)
    for i in range(int((len(num)+1)/2)):
        lchar, rchar = num[i], num[-1*(i+1)]
        debug(f'{lchar} :: {rchar}')
        if lchar != rchar:
            return False
    return True

def solve(args):
    solution = None
    debug(isPalindrome(args.test))
    return solution

if __name__ == '__main__':
    page = 'https://projecteuler.net/problem=4'
    problem = 'A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99. Find the largest palindrome made from the product of two 3-digit numbers.'
    args = getArgs()
    tic = time.time(); solution = solve(args); toc = time.time()
    if args.verbose: print()
    print(f'[{timedelta(seconds=toc-tic)}] \033[1m\033[92manswer\033[0m: {solution}')
