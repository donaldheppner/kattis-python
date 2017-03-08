import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()

class Room:
    lower_bound = 0
    upper_bound = 0

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __init__(self, minion):
        self.lower_bound = minion[0]
        self.upper_bound = minion[1]

    def in_range(self, minion):
        return self.lower_bound <= minion[0] <= self.upper_bound or self.upper_bound >= minion[1] >= self.lower_bound

    def add(self, minion):
        self.lower_bound = max(self.lower_bound, minion[0])
        self.upper_bound = min(self.upper_bound, minion[1])


def solve(input, output):
    number_of_minions = int(input.readline())
    minions = [None] * number_of_minions
    for i in range(0, number_of_minions):
        minions[i] = tuple(map(int, input.readline().split()))

    # sort the minions
    minions = sorted(minions, key=lambda x: x[0])

    rooms = [Room(minions[0])]
    for minion in minions[1:]:
        if rooms[-1].in_range(minion):
            rooms[-1].add(minion)
        else:
            rooms.append(Room(minion))

    output.write("{}".format(len(rooms)))


if __name__ == '__main__':
    main()
