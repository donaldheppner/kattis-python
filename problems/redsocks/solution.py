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

        step = 1
        prob = probability(socks)
        step_function = increase_red if prob < ratio else increase_black
        while True:
            if prob == ratio:
                output.write("{} {}\n".format(socks[0], socks[1]))
                break

            if socks[0] + socks[1] > 50000 and step == 1:
                output.write("impossible\n")
                break

            if prob < ratio:
                if step_function == increase_black:
                    # overshot, back it up
                    if step > 1:
                        socks[1] -= step
                        step //= 10
                    else:
                        # swap function
                        step_function = increase_red
                else:
                    step *= 10
            else:
                if step_function == increase_red:
                    # overshot, back it up
                    if step > 1:
                        socks[0] -= step
                        step //= 10
                    else:
                        # swap function
                        step_function = increase_black
                else:
                    step *= 10

            step_function(socks, step)
            prob = probability(socks)

if __name__ == '__main__':
    main()
