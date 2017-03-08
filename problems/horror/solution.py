import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


INFINITY = 999999


def compute_indexes(indexes, graph, start):
    for i in graph[start]:
        # backtracking if the indexes aren't shrinking
        if indexes[i] > indexes[start] + 1:
            indexes[i] = indexes[start] + 1
            compute_indexes(indexes, graph, i)


def solve(input, output):
    number_movies, number_horror_movies, number_similarities = map(int, input.readline().split())
    horror_movies = set(map(int, input.readline().split()))
    similarities = [None] * number_similarities

    # store all the relationships in a graph
    graph = {key: list() for key in range(0, number_movies)}
    for i in range(0, number_similarities):
        similarity = tuple(map(int, input.readline().split()))
        graph[similarity[0]].append(similarity[1])
        graph[similarity[1]].append(similarity[0])

    # set everything to infinity
    horror_indexes = [INFINITY] * number_movies

    # set up the horror list
    for i in horror_movies:
        horror_indexes[i] = 0

    for i in horror_movies:
        compute_indexes(horror_indexes, graph, i)

    # get the value of the highest horror index
    max_hi = max(horror_indexes)
    output.write("{}".format(horror_indexes.index(max_hi)))


if __name__ == '__main__':
    main()
