import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


INFINITY = 999999


def solve(input, output):
    number_movies, number_horror_movies, number_similarities = map(int, input.readline().split())
    horror_movies = set(map(int, input.readline().split()))
    similarities = [None] * number_similarities

    for i in range(0, number_similarities):
        similarities[i] = tuple(map(int, input.readline().split()))

    horror_indexes = [INFINITY] * number_movies

    # set up the horror list
    for i in horror_movies:
        horror_indexes[i] = 0

    for similarity in similarities:
        # the larger value = the smaller value + 1
        if horror_indexes[similarity[0]] > horror_indexes[similarity[1]]:
            horror_indexes[similarity[0]] = horror_indexes[similarity[1]] + 1
        elif horror_indexes[similarity[0]] < horror_indexes[similarity[1]]:
            horror_indexes[similarity[1]] = horror_indexes[similarity[0]] + 1

    # get the value of the highest horror index
    max_hi = max(horror_indexes)

    output.write("{}".format(horror_indexes.index(max_hi)))


if __name__ == '__main__':
    main()
