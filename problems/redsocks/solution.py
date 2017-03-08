import sys
import time

def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def probability(socks):
    return (socks[0] / (socks[0] + socks[1])) * ((socks[0] - 1) / (socks[0] + socks[1] - 1))


def increase_red(socks, step=1):
    socks[0] += step


def increase_black(socks, step=1):
    socks[1] += step


NONE = 0
INCREASE_RED = 1
INCREASE_BLACK = 2


def solve(input, output):
    start_time = time.perf_counter()

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
        socks = [2, 1]  # must have a minimum of two red socks and 1 black sock

        while True:
            prob = probability(socks)
            if prob == ratio:
                output.write("{} {}\n".format(socks[0], socks[1]))
                break

            if socks[0] + socks[1] > 50000:
                output.write("impossible")
                break

            if prob < ratio:
                # switch to red
                step_function = increase_red    # increase numerator
            else:
                # switched to black
                step_function = increase_black  # increase denominator

            step_function(socks)

    sys.stderr.write("Runtime: {}\n".format(time.perf_counter() - start_time))

if __name__ == '__main__':
    main()
