import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def distanceFromZero(number, dimension):
    lastAdded = False
    distance = 0
    for position in range(0, dimension):
        c = number[position]
        if lastAdded:
            if c == '0':
                distance += (2 ** (dimension - position - 1))
                lastAdded = True
            else:
                lastAdded = False
        else:
            if c == '1':
                distance += (2 ** (dimension - position - 1))
                lastAdded = True
            else:
                lastAdded = False

    return distance


def solve(input, output):
    line = input.readline()
    (d, start, end) = (map(str, line.split(" ")))
    dimension = int(d)

    a = distanceFromZero(start, dimension)
    b = distanceFromZero(end, dimension)

    output.write(str(b - a - 1))


if __name__ == '__main__':
    main()
