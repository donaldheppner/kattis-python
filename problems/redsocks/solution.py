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
        elif p == 0:
            output.write("0 2\n")
        elif p == q:
            output.write("2 0\n")
        else:

            # initialized the test
            red = 2
            for total in range(2, 50001):
                tp = total * (total - 1) * p

                while red * (red - 1) * q < tp:
                    red += 1
                else:
                    if red * (red - 1) * q == tp:
                        output.write("{} {}\n".format(red, total - red))
                        break
            else:
                output.write("impossible\n")


if __name__ == '__main__':
    main()
