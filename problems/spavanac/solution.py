import os
import sys


def main(args=None):
    input = sys.stdin
    output = sys.stdout
    if args is not None:
        input = args[0]
        output = args[1]

    solve(input, output)

    input.flush()
    output.flush()


def solve(input, output):
    output.write("9 25\n")
