import sys
import math

rank_points = (
    100, 75, 60, 50, 45, 40, 36, 32, 29, 26, 24, 22, 20, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


class Contestant:
    def __init__(self, x, s, p, f, o):
        self.x = x
        self.s = s
        self.p = p
        self.f = f
        self.o = o
        self.points = 0

    def did_participate(self):
        return (self.s + self.p + self.f + self.o) != 0

    def is_tied(self, c):
        return self.s == c.s and self.p == c.p and self.f == c.f

    def calc_with_points(self, points):
        self.points = 0 if not self.did_participate() else points + self.o

    def calc_with_rank(self, rank):
        self.calc_with_points(0 if rank >= 30 else rank_points[rank])

    def calc_tie_points(self, start, end):
        total_points = sum(rank_points[start:min(end + 1, 30)])
        avg_points = math.ceil(total_points / float((end + 1 - start)))

        self.calc_with_points(avg_points)


def calc_tie(contestants, start, end):
    for contestant in contestants[start:(end + 1)]:
        contestant.calc_tie_points(start, end)


def solve(input, output):
    num_lines = int(input.readline())
    contestants = list()
    for x in range(0, num_lines):
        (s, p, f, o) = map(int, input.readline().split())
        contestants.append(Contestant(x, s, p, f, o))

    sorted_contestants = sorted(contestants, key=lambda c: (-c.s, c.p, c.f))
    start_tie = -1
    for x in range(0, len(sorted_contestants) - 1):
        contestant = sorted_contestants[x]
        if sorted_contestants[x].is_tied(sorted_contestants[x + 1]):
            if start_tie == -1:
                start_tie = x
            continue
        else:
            if start_tie == -1:  # simple points calculation
                contestant.calc_with_rank(x)
            else:  # ending a tie, this contestant is not tied with the next one
                calc_tie(sorted_contestants, start_tie, x)
                start_tie = -1

    # handle last element
    if start_tie == -1:
        sorted_contestants[-1].calc_with_rank(len(sorted_contestants) - 1)
    else:
        calc_tie(sorted_contestants, start_tie, len(sorted_contestants) - 1)

    for con in sorted(sorted_contestants, key=lambda c: c.x):
        output.write(str(con.points) + "\n")


if __name__ == '__main__':
    main()
