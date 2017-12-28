import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def in_region(r1, r2, map, visited):
    if r1 == r2:
        return True
    elif r1 in map:
        nv = visited.copy()
        nv.add(r1)
        for r in (map[r1] - nv):
            if in_region(r, r2, map, nv):
                return True
        else:
            return False
    else:
        return False


def get_region(r1, map, visited):
    visited.add(r1)
    if r1 in map:
        for r in (map[r1] - visited):
            get_region(r, map, visited)

    return visited

def solve(input, output):
    (rows, columns) = map(int, input.readline().split())

    region_map = [[0 for x in range(columns)] for y in range(rows)]
    region_count = 0

    lines = []
    for row in range(0, rows):
        lines.append(input.readline())

    equivalents = dict()

    for row in range(0, rows):
        for column in range(0, columns):
            val = lines[row][column]
            if row > 0 and lines[row - 1][column] == val:  # if top matches val, then we're the same region
                region_map[row][column] = region_map[row - 1][column]
                # if back also matches on value but they do not share an id, then map the regions as equivalent
                if lines[row][column - 1] == val and region_map[row][column - 1] != region_map[row][column]:
                    a = region_map[row][column - 1]
                    b = region_map[row][column]
                    if a in equivalents:
                        equivalents[a].add(b)
                    else:
                        equivalents[a] = set([b])

                    if b in equivalents:
                        equivalents[b].add(a)
                    else:
                        equivalents[b] = set([a])
            elif column > 0 and lines[row][column - 1] == val:  # if back matches val, then we're the same region
                region_map[row][column] = region_map[row][column - 1]
            else:  # new region
                region_count += 1
                region_map[row][column] = region_count

    # simplify the region map
    regions = [None] * (region_count + 1)
    for r in range(1, len(regions)):
        if regions[r] is None:
            s = get_region(r, equivalents, set())
            for x in s:
                regions[x] = s

    num_queries = int(input.readline())
    for x in range(0, num_queries):
        (r1, c1, r2, c2) = map(int, input.readline().split())
        region1 = region_map[r1 - 1][c1 - 1]
        region2 = region_map[r2 - 1][c2 - 1]
        #if in_region(region1, region2, equivalents, set()):
        if region1 == region2 or region2 in regions[region1]:
            output.write("binary" if lines[r1 - 1][c1 - 1] == '0' else "decimal")
        else:
            # traverse equivalents map
            output.write("neither")
        output.write("\n")


if __name__ == '__main__':
    main()
