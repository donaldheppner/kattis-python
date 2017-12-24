import sys
import math

def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def combo(n, r):
    return math.factorial(n)//(math.factorial(r) * math.factorial(n - r))


def cn(c):
    return (combo(2 * c, c))//(c + 1)


def s(n):
    result = 0
    for m in range(0, n + 1):
        f = cn(m)
        g = cn(n - m)
        result += (f * g)

    return result


def solve(input, output):
    n = int(input.readline())

    output.write(str(int(s(n))))


if __name__ == '__main__':
    main()
