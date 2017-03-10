import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


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
        red = 2
        total = 3

        while True:
            delta = (p * ((total * total) - total)) - (q * ((red * red) - red))

            if delta == 0:
                output.write("{} {}\n".format(red, total - red))
                break
            elif delta < 0:
                total += 1
            else:
                red += 1

            if total > 50000:
                output.write("impossible\n")
                break


if __name__ == '__main__':
    main()
