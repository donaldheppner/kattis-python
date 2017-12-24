import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


class Key:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Region:
    def __init__(self, id):
        self.id = Key(id)

    def __str__(self):
        return str(self.id.value)


def solve(input, output):
    (rows, columns) = map(int, input.readline().split())

    region_map = [[0 for x in range(columns)] for y in range(rows)]
    region_count = 0

    lines = []
    for row in range(0, rows):
        lines.append(input.readline())

    for row in range(0, rows):
        for column in range(0, columns):
            val = lines[row][column]
            if row > 0 and lines[row - 1][column] == val:  # if top matches val, then we're the same region
                region_map[row][column] = region_map[row - 1][column]
                # if back also matches on value but they do not share an id, then merge regions by
                # assigning current and back the min_id
                if lines[row][column - 1] == val and region_map[row][column - 1].id.value != region_map[row][column].id.value:
                    min_id = region_map[row][column - 1].id if region_map[row][column - 1].id.value < region_map[row][column].id.value else region_map[row][column].id
                    region_map[row][column].id = min_id
                    region_map[row][column - 1].id = min_id
            elif column > 0 and lines[row][column - 1] == val:  # if back matches val, then we're the same region
                region_map[row][column] = region_map[row][column - 1]
            else:  # new region
                region_count += 1
                region_map[row][column] = Region(region_count)

    num_queries = int(input.readline())
    for x in range(0, num_queries):
        (r1, c1, r2, c2) = map(int, input.readline().split())
        region1 = region_map[r1 - 1][c1 - 1]
        region2 = region_map[r2 - 1][c2 - 1]
        if region1.id.value == region2.id.value:
            output.write("binary" if lines[r1 - 1][c1 - 1] == '0' else "decimal")
        else:
            output.write("neither")
        output.write("\n")


if __name__ == '__main__':
    main()
