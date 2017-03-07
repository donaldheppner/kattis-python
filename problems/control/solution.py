import sys


def main():
    input = sys.stdin
    output = sys.stdout

    solve(input, output)

    input.flush()
    output.flush()


def solve(input, output):
    number_of_recipes = int(input.readline())

    # create a list of sets for each recipe; skip the first number as it is the number of ingredients
    recipes = [None] * number_of_recipes
    for recipe_number in range(0, number_of_recipes):
        recipes[recipe_number] = frozenset(map(int, input.readline().split()[1:]))

    concocted_count = 0
    ingredient_cauldrons = {}
    used_ingredients = set()

    for recipe in recipes:
        used_remaining_ingredients = recipe & used_ingredients
        while len(used_remaining_ingredients) != 0:
            # funky notation to get an item from a set
            candidate_cauldron = ingredient_cauldrons[next(iter(used_remaining_ingredients))]
            if candidate_cauldron <= recipe:
                used_remaining_ingredients -= candidate_cauldron
            else:
                # can't make it work
                break
        else:
            # we did it!
            concocted_count += 1
            # update our list of used ingredients
            used_ingredients |= recipe
            # update our recipe:cauldron dictionary
            for ingredient in recipe:
                ingredient_cauldrons[ingredient] = recipe

    output.write("{}".format(concocted_count))


if __name__ == '__main__':
    main()
