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

        while True:
            prob = calc(red, total)
            if prob < ratio:
                red += 1
            elif prob > ratio:
                total += 1
            else:
                output.write("{} {}\n".format(red, total - red))
                break

            if total > 50000:
                output.write("impossible\n")
                break


if __name__ == '__main__':
    main()
