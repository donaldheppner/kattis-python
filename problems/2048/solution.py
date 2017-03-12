import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def calculate_row(row):
    i = 0
    while i < len(row):
        if row[i] == 0:
            row.pop(i)
            continue

        if i < len(row) - 1:
            if row[i + 1] == row[i]:
                row[i] *= 2
                row.pop(i + 1)

        i += 1

    while len(row) < 4:
        row.append(0)


def solve(input, output):
    grid = []
    for i in range(0, 4):
        grid.append([map(int, input.readline().split())])

    direction = int(input.readline())

    if direction == 0:
        # left
        for row in grid:
            calculate_row(row)

    elif direction == 1:
        # up
        for i in range(0, 4):
            row = [grid[i][x] for x in range(0, 4)]
            calculate_row(row)
            for x in range(0, 4):
                grid[i][x] = row[x]

    elif direction == 2:
        # right
        for row in grid:
            row.reverse()
            calculate_row(row)
            row.reverse()
    elif direction == 3:
        # down
        for i in range(0, 4):
            row = [grid[i][x] for x in range(0, 4)]
            row.reverse()
            calculate_row(row)
            row.reverse()
            for x in range(3, 1):
                grid[i][x] = row[x]

    for row in grid:
        output.write(" ".join(map(str, row)))
        output.write("\n")


if __name__ == '__main__':
    main()
