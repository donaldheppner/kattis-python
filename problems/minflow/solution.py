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
        self.number = args[0]
        self.x = args[1]
        self.y = args[2]
        self.z = args[3]
        self.holes = args[4]

    def __repr__(self):
        return str(self.number)

    def add_pipe(self, j):
        self.connected_junctions.add(j)
        j.connected_junctions.add(self)

    def distance_cost(self, j):
        return 0 if j in self.connected_junctions else self.distance(j)

    def distance(self, j):
        return (((self.x - j.x) ** 2) + ((self.y - j.y) ** 2) + ((self.z - j.z) ** 2)) ** .5

    def can_connect(self, j, path):
        used_holes = 0

        try:
            self_index = path.index(self)
            if self_index > 0:
                used_holes = 0 if path[self_index - 1] in self.connected_junctions else 1
        except ValueError:
            used_holes = 0

        return j in self.connected_junctions or (self.holes - used_holes > 0 and j.holes > 0)

    # how many holes are used by connecting from self to junction; could be 0 of existing pipes
    def used_holes(self, j):
        return 0 if j == self or j in self.connected_junctions else 1

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
        distance_cost += path[i].distance_cost(path[i + 1])

    return hole_cost + distance_cost + calculate_downhill_cost(path)


def calculate_downhill_cost(path):
    downhill_junctions = set()
    max_z = max([x.z for x in path])

    # get junctions connected by existing pipes that are downhill based on max Z (pressure)
    for junction in path:
        for connected_junction in [x for x in junction.connected_junctions if x not in path and x.z <= max_z]:
            add_downhill_junctions(connected_junction, path, max_z, downhill_junctions)

    return sum(x.holes for x in downhill_junctions) * 0.5


def add_downhill_junctions(junction, path, max_z, downhill_junctions):
    downhill_junctions.add(junction)
    for connected_junction in [x for x in junction.connected_junctions if
                               x not in path and x not in downhill_junctions and x.z <= max_z]:
        add_downhill_junctions(connected_junction, path, max_z, downhill_junctions)


def print_path(path, cost):
    sys.stderr.write(" ".join([str(x.number) for x in path]))
    sys.stderr.write(": {}\n".format(cost))


def find_min_cost(current, target, all, path):
    path.append(current)
    if current == target:
        cost = calculate_cost(path)
        print_path(path, cost)
        return cost

    costs = [2 ** 32]
    for next_junction in [x for x in all if x not in path and current.can_connect(x, path)]:
        costs.append(find_min_cost(next_junction, target, all, path.copy()))

    return min(costs)


def solve(input, output):
    case = 0
    while True:
        case += 1
        line = input.readline()
        if len(line) == 0:
            break

        (number_of_junctions, number_of_pipes) = map(int, line.split())
        junctions = []
        pipes = {}
        for i in range(0, number_of_junctions):
            j = [x for x in map(int, input.readline().split())]
            j.insert(0, i)  # store junction number
            junctions[i] = Junction(j)

        for i in range(0, number_of_pipes):
            (j1, j2) = map(int, input.readline().split())
            pipes.add(j1 - 1, j2 - 1)
            pipes.add(j2 - 1, j1 - 1)

        costs = [2 ** 32]
        j_stack = [junctions[0]]
        while len(j_stack) != 0:
            last_juction = j_stack[-1]
            if last_juction.number < number_of_junctions:
                j_stack.append(junctions[last_juction.number + 1])
                continue
            else:
                # calculate








        min_cost = find_min_cost(junctions[1], junctions[number_of_junctions], [x for x in junctions.values()], [])

        output.write("Case {}: ".format(case))
        if min_cost == 2 ** 32:
            output.write("impossible\n")
        else:
            output.write("{0:.4f}\n".format(min_cost))


if __name__ == '__main__':
    main()
