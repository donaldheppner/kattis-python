import sys
import heapq


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
        recipes[recipe_number] = set(map(int, input.readline().split()[1:]))

    concocted_count = 0

    # indexed based on the first ingredient; if it is in there we can do it, if not we
    # know it must be combined with something else
    ingredient_cauldrons = {}
    used_ingredients = set()

    for recipe in recipes:
        used_remaining_ingredients = list(recipe & used_ingredients)
        heapq.heapify(used_remaining_ingredients)

        # if recipe uses only fresh ingredients
        if len(used_remaining_ingredients) == 0:
            # ignore cauldrons with one ingredient, treat as unused
            if len(recipe) > 1:
                # add the cauldron and continue
                ingredient_cauldrons[min(recipe)] = recipe
                used_ingredients |= recipe

            concocted_count += 1
            continue

        first_ingredients = set()   # the index for the cauldrons dictionary
        mixed_ingredients = set()   # track those already in the recipe
        while len(used_remaining_ingredients) != 0:
            # get the next first ingredient, skipping those already in the mix
            while len(used_remaining_ingredients) > 0:
                first_ingredient = heapq.heappop(used_remaining_ingredients)
                if first_ingredient not in mixed_ingredients:
                    break
            else:
                continue   # all done with used ingredients, this will run the else clause of the while loop (as opposed to breaking here)

            # see if a cauldron exists matching the first ingredient
            candidate_cauldron = ingredient_cauldrons.get(first_ingredient)
            if candidate_cauldron is not None:
                if candidate_cauldron <= recipe:
                    mixed_ingredients |= candidate_cauldron     # store the ingredients we've mixed, this will help with popping from the heap
                    first_ingredients.add(first_ingredient)     # record this as a cauldron we intend to mix/destroy
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
                    del ingredient_cauldrons[f]

            # store new recipe
            ingredient_cauldrons[min(recipe)] = recipe

    output.write("{}".format(concocted_count))


if __name__ == '__main__':
    main()
