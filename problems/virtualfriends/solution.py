import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def solve(input, output):
    number_of_testcases = int(input.readline())
    for test_case in range(0, number_of_testcases):
        number_of_friendships = int(input.readline())
        people = {}
        for friendship in range(0, number_of_friendships):
            a, b = input.readline().split()
            if a not in people:
                people[a] = set([a])
            if b not in people:
                people[b] = set([b])

            # already in the network
            if b in people[a]:
                output.write("{}\n".format(len(people[a])))
                continue

            biggest_friend = a if len(people[a]) > len(people[b]) else b
            smallest_friend = a if b == biggest_friend else b

            smallest_friends = people[smallest_friend]
            biggest_friends = people[biggest_friend]
            # point all of smallest's friends to biggest's network
            for smallest_friend in smallest_friends:
                people[smallest_friend] = biggest_friends

            # update the network for all
            biggest_friends.update(smallest_friends)

            output.write("{}\n".format(len(biggest_friends)))


if __name__ == '__main__':
    main()
