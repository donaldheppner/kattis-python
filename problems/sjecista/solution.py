import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def solve(input, output):
    number_of_points = int(input.read())
    intersections = 0

    for point in range(1, number_of_points - 2):
        intersections += sum([i * point for i in range(1, number_of_points - point - 1)])

    output.write("{}".format(intersections))

if __name__ == '__main__':
    main()
