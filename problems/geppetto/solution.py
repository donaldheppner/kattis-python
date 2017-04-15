import sys
import math

def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def combinations(n, r):
    return 0 if r > n else math.factorial(n)//(math.factorial(r) * math.factorial(n - r))


# combinations of size start->n
def all_combinations(n, start = 0):
    result = 0
    for x in range(start, n + 1):
        result += combinations(n, x)

    return result


def solve(input, output):
    (number_ingredients, number_bad_pairs) = (map(int, input.readline().split(" ")))
    total_pizzas = all_combinations(number_ingredients)

    # loading all the bad pairs in a set will remove duplicates
    bad_pairs = set()
    for x in range(0, number_bad_pairs):
        bad_pairs.add(frozenset(map(int, input.readline().split(" "))))

    # initialize the lookup
    bad_pair_lookup = {}
    for x in range(1, number_ingredients + 1):
        bad_pair_lookup[x] = set()

    first = True
    pizzas_to_remove = 0
    removed_pairs = 0
    for pair_set in bad_pairs:
        pair_list = [x for x in pair_set]

        if first:
            pizzas_to_remove += all_combinations(number_ingredients - 2)
            first = False
        else:
            first_ingredient_pairs = bad_pair_lookup[pair_list[0]]
            second_ingredient_pairs = bad_pair_lookup[pair_list[1]]
            overlap = len(first_ingredient_pairs) + len(second_ingredient_pairs)

            possible_pizzas_to_remove = all_combinations(number_ingredients - 2 - overlap)
            if overlap == 0:
                possible_pizzas_to_remove -= sum(all_combinations(number_ingredients - 4 - x) for x in range(0, removed_pairs + 1))

            pizzas_to_remove += max(1, possible_pizzas_to_remove)

        bad_pair_lookup[pair_list[0]].add(pair_list[1])
        bad_pair_lookup[pair_list[1]].add(pair_list[0])
        removed_pairs += 1

    output.write(str(total_pizzas - pizzas_to_remove))


if __name__ == '__main__':
    main()
