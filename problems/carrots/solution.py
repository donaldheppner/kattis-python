import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def solve(input, output):
    output.write(input.readline().split(" ")[1])


if __name__ == '__main__':
    main()
