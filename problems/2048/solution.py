import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def calculate_row(row):

    # remove all the zeros
    row = [x for x in row if x != 0]

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

    return row


def solve(input, output):
    grid = []
    for i in range(0, 4):
        row = [x for x in map(int, input.readline().split())]
        grid.append(row)

    direction = int(input.readline())

    if direction == 0:
        # left
        for i in range(0, 4):
            grid[i] = calculate_row(grid[i])

    elif direction == 1:
        # up
        for i in range(0, 4):
            row = [grid[x][i] for x in range(0, 4)]
            row = calculate_row(row)
            for x in range(0, 4):
                grid[x][i] = row[x]

    elif direction == 2:
        # right
        for i in range(0, 4):
            grid[i].reverse()
            row = calculate_row(grid[i])
            row.reverse()
            grid[i] = row
    elif direction == 3:
        # down
        for i in range(0, 4):
            row = [grid[x][i] for x in range(0, 4)]
            row.reverse()
            row = calculate_row(row)
            row.reverse()
            for x in range(0, 4):
                grid[x][i] = row[x]

    for row in grid:
        output.write(" ".join(map(str, row)))
        output.write("\n")


if __name__ == '__main__':
    main()
