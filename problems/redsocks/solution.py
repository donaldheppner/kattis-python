import sys
import time


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def calc(red, total):
    return (red * (red - 1)) / (total * (total - 1))


def solve(input, output):
    while True:
        p, q = map(int, input.readline().split())
        if p == 0 and q == 0:
            break
        elif p / q == 0:
            output.write("0 2\n")
            continue
        elif p / q == 1:
            output.write("2 0\n")
            continue

        # initialized the test
        ratio = p / q
        red = 2
        total = 3

        # find the total value
        while (not (ratio * ((total * total) - total)).is_integer()) and total <= 49998:
            total += 1

        # find the red value
        if total <= 49998:
            reds_squared_minus_red = ratio * ((total * total) - total)
            while (red * red) - red < reds_squared_minus_red:
                red += 1 # TODO: if red > total - 2, recompute total
            else:
                output.write("{} {}\n".format(red, total - red))
        else:
            output.write("impossible\n")


if __name__ == '__main__':
    main()
