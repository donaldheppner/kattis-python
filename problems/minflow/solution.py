import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


class Junction:
    connected_pipes = []

    def __init__(self, x, y, z, holes):
        self.x = x
        self.y = y
        self.z = z
        self.holes = holes

    def add_pipe(self, j):
        self.connected_pipes.append(j)
        j.add_pipe(self)

    def distance(self, j):
        return (((self.x - j.x) ** 2) + ((self.y - j.y) ** 2) + ((self.y - j.y) ** 2)) ** .5


def solve(input, output):
    while True:
        (number_junctions, number_of_pipes) = map(int, input.readline().split())
        junctions = {}
        for i in range(1, number_junctions + 1):
            junctions[i] = Junction(map(int, input.readline().split()))

        for i in range(0, number_of_pipes):
            (j1, j2) = map(int, input.readline().split())
            junctions[j1].add_pipe(j2)



if __name__ == '__main__':
    main()
