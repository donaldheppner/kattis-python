import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


class Junction:
    def __init__(self, args):
        self.connected_junctions = set()
        self.x = args[0]
        self.y = args[1]
        self.z = args[2]
        self.holes = args[3]

    def add_pipe(self, j):
        self.connected_junctions.add(j)
        j.connected_junctions.add(self)

    def distance(self, j):
        return (((self.x - j.x) ** 2) + ((self.y - j.y) ** 2) + ((self.z - j.z) ** 2)) ** .5

    def can_connect(self, j, used_holes=0):
        return j in self.connected_junctions or (self.holes - used_holes > 0 and j.holes > 0)

    # how many holes are used by connecting from self to junction; could be 0 of existing pipes
    def used_holes(self, j):
        return 0 if j in self.connected_junctions else 1

    def requires_pipe(self, j):
        return not (j in self.connected_junctions or j == self)


def calculate_cost(path):
    if len(path) == 1:
        return path[0].holes * 0.5

    hole_cost = 0
    for i in range(0, len(path)):
        used_holes = 0
        if i > 0 and path[i].requires_pipe(path[i - 1]):
            used_holes += 1
        if i < len(path) - 1 and path[i].requires_pipe(path[i + 1]):
            used_holes += 1

        hole_cost += ((path[i].holes - used_holes) * .5)

    distance_cost = 0
    for i in range(0, len(path) - 1):
        distance_cost += path[i].distance(path[i + 1])

    return hole_cost + distance_cost + calculate_downhill_cost(path)


def calculate_downhill_cost(path):
    downhill_junctions = set()
    max_z = max([x.z for x in path])

    # get junctions connected by existing pipes that are downhill based on max Z (pressure)
    for junction in path:
        for connected_junction in [x for x in junction.connected_junctions if x not in path and x.z <= max_z]:
            add_downhill_junctions(connected_junction, path, max_z, downhill_junctions)

    return sum(x.holes for x in downhill_junctions)


def add_downhill_junctions(junction, path, max_z, downhill_junctions):
    downhill_junctions.add(junction)
    for connected_junction in [x for x in junction.connected_junctions if
                               x not in path and x not in downhill_junctions and x.z <= max_z]:
        add_downhill_junctions(connected_junction, path, max_z, downhill_junctions)


def find_min_cost(current, target, all, path=[]):
    costs = [2 ** 32]
    for next_junction in [x for x in all if x != current and x not in path]:
        # can I connect? used holes calculated based on what it cost current to connect to the previous node
        if current.can_connect(next_junction, 0 if len(path) == 0 else current.used_holes(path[-1])):
            if next_junction == target:
                # calculate costs
                new_path = path.copy()
                new_path.append(next_junction)
                costs.append(calculate_cost(path))

            else:
                new_path = path.copy()
                new_path.append(current)
                costs.append(find_min_cost(next_junction, target, all, new_path))

    return min(costs)


def solve(input, output):
    case = 0
    while True:
        case += 1
        line = input.readline()
        if len(line) == 0:
            break

        (number_of_junctions, number_of_pipes) = map(int, line.split())
        junctions = {}
        for i in range(1, number_of_junctions + 1):
            j = tuple(x for x in map(int, input.readline().split()))
            junctions[i] = Junction(j)

        for i in range(0, number_of_pipes):
            (j1, j2) = map(int, input.readline().split())
            junctions[j1].add_pipe(junctions[j2])

        min_cost = find_min_cost(junctions[1], junctions[number_of_junctions], junctions.values())

        output.write("Case {}: ".format(case))
        if min_cost == 2 ** 32:
            output.write("impossible\n")
        else:
            output.write("{0:.4f}\n".format(min_cost))


if __name__ == '__main__':
    main()
