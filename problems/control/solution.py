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

    # indexed based on the first ingredient; if it is in there we can do it, if not we
    # know it must be combined with something else
    ingredient_cauldrons = {}

    used_ingredients = set()

    for recipe in recipes:
        used_remaining_ingredients = recipe & used_ingredients

        # if no used ingredients and recipe is just one ingredient, consider it unused (got us to 19/40)
        if len(used_remaining_ingredients) == 0 and len(recipe) == 1:
            concocted_count += 1
            continue

        first_ingredients = set()
        while len(used_remaining_ingredients) != 0:
            first_ingredient = min(used_remaining_ingredients)
            if first_ingredient in ingredient_cauldrons:
                candidate_cauldron = ingredient_cauldrons[first_ingredient]
                if candidate_cauldron <= recipe:
                    used_remaining_ingredients -= candidate_cauldron
                    first_ingredients.add(first_ingredient)
                else:
                    # can't make it work, the cauldron isn't a subset of the recipe
                    break
            else:
                # can't make it work, none of our cauldrons have a matching first ingredient
                break
        else:
            # we did it!
            concocted_count += 1
            # update our list of used ingredients
            used_ingredients |= recipe

            # update our recipe:cauldron dictionary; remove used recipes
            if len(first_ingredients) > 0:
                for f in first_ingredients:
                    ingredient_cauldrons.pop(f)

            ingredient_cauldrons[min(recipe)] = recipe

    output.write("{}".format(concocted_count))


if __name__ == '__main__':
    main()
