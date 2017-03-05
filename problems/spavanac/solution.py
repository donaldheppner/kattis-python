import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def solve(input, output):
    line = input.readline()
    (hour, minute) = map(int, line.split(" "))

    if minute >= 45:
        minute -= 45
    else:
        minute = minute + 60 - 45
        if hour != 0:
            hour -= 1
        else:
            hour = 23

    output.write("{} {}\n".format(hour, minute))
