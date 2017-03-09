import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def calc(red, total):
    return 1 if total - red == 0 else (red * (red - 1)) / (total * (total - 1))


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
            # find the next possible total value
            total += 1

            # find the red value
            if total <= 49998:
                reds_squared_minus_red = ratio * ((total * total) - total)
                while (red * red) - red < reds_squared_minus_red:
                    red += 1
                else:
                    prob = calc(red, total)
                    if prob == ratio:
                        output.write("{} {}\n".format(red, total - red))
                        break
                    elif prob < ratio:
                        red += 1
                        total += 1
                    else:
                        total += 1
            else:
                output.write("impossible\n")
                break



if __name__ == '__main__':
    main()
