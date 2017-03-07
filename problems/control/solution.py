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
        if len(recipe & used_ingredients) == 0: # recipe doesn't use any already used ingredients
            for ingredient in recipe
                ingredient_cauldrons[ingredient]
            cauldrons.add(recipe)               # record the cauldron
            used_ingredients |= recipe          # note the used ingredients, union sets
            concocted_count += 1
        else: # can I combine cauldrons?
            candidate_cauldrons = set()
            remaining_ingredients = recipe.copy()
            for cauldron in cauldrons:
                if cauldron <= recipe:
                    candidate_cauldrons.add(cauldron)
                    remaining_ingredients -= cauldron
                    if len(remaining_ingredients & used_ingredients) == 0:
                        # success! mix the ingredients and record the new cauldron
                        used_ingredients |= remaining_ingredients
                        for c in candidate_cauldrons:
                            cauldrons.discard(c)
                        cauldrons.add(recipe)
                        concocted_count += 1
                        break

    output.write("{}".format(concocted_count))


if __name__ == '__main__':
    main()
