import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def solve(input, output):
    input.readline() #skip first line, just split the next one
    balloons = map(int, input.readline().split(' '))

    arrows = dict()     # all our live arrows
    arrow_count = 0     # the answer, easier than summing values at the end
    for balloon in balloons:
        if balloon in arrows:   # use the arrow at that height
            arrow = arrows[balloon]
            if arrow == 1:
                del arrows[balloon]
            else:
                arrows[balloon] = arrow - 1
        else:                   # create a new arrow
            arrow_count += 1

        # add an arrow at the height below the balloon
        if (balloon - 1) in arrows:
            arrows[balloon - 1] += 1
        else:
            arrows[balloon - 1] = 1

    output.write(str(arrow_count))


if __name__ == '__main__':
    main()
