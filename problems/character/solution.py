import sys
import math


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def solve(input, output):
    num_characters = int(input.readline())

    num_relationships = 0
    if num_characters > 1:
        for x in range(2, num_characters + 1):
            num_relationships += (math.factorial(num_characters) // (math.factorial(x) * math.factorial(num_characters - x)))

    output.write(str(num_relationships))


if __name__ == '__main__':
    main()
