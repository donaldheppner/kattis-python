import sys
import time

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

    log = sys.stderr
    is_target_problem = recipe_number == 50000 - 1
    is_target_recipe = False
    start_time = time.perf_counter()

    if is_target_problem:
        log.write("At target problem!\n")

    for recipe in recipes:
        if is_target_problem and (len(recipe) > 2):
            log.write("Got to final recipe in: {} seconds\n".format(time.perf_counter() - start_time))
            is_target_recipe = True

        if is_target_recipe:
            comp_time = time.perf_counter()
        used_remaining_ingredients = recipe & used_ingredients
        if is_target_recipe:
            log.write("used_remaining_ingredients union: {} seconds\n".format(time.perf_counter() - comp_time))

        # if no used ingredients and recipe is just one ingredient, consider it unused (got us to 19/40)
        if len(used_remaining_ingredients) == 0 and len(recipe) == 1:
            concocted_count += 1
            continue

        total_set_add_time = 0.0
        total_set_intersection_time = 0.0

        first_ingredients = set()
        while len(used_remaining_ingredients) != 0:
            first_ingredient = min(used_remaining_ingredients)
            candidate_cauldron = ingredient_cauldrons.get(first_ingredient)
            if candidate_cauldron is not None:
                if candidate_cauldron <= recipe:
                    if is_target_recipe:
                        set_intersection_time = time.perf_counter()
                    used_remaining_ingredients -= candidate_cauldron
                    if is_target_recipe:
                        total_set_intersection_time += time.perf_counter() - set_intersection_time

                    if is_target_recipe:
                        set_add_time = time.perf_counter()
                    first_ingredients.add(first_ingredient)
                    if is_target_recipe:
                        total_set_add_time += time.perf_counter() - set_add_time
                else:
                    # can't make it work, the cauldron isn't a subset of the recipe
                    break
            else:
                # can't make it work, none of our cauldrons have a matching first ingredient
                break
        else:
            if is_target_recipe:
                clean_up_time = time.perf_counter()
            # we did it!
            concocted_count += 1
            # update our list of used ingredients
            used_ingredients |= recipe

            # update our recipe:cauldron dictionary; remove used recipes
            if len(first_ingredients) > 0:
                for f in first_ingredients:
                    del ingredient_cauldrons[f]

            ingredient_cauldrons[min(recipe)] = recipe

            if is_target_recipe:
                log.write("Clean up time: {} seconds\n".format(time.perf_counter() - clean_up_time))

    if is_target_problem:
        log.write("Total set intersection time: {} seconds\n".format(total_set_intersection_time))
        log.write("Total set add time: {} seconds\n".format(total_set_add_time))

    output.write("{}".format(concocted_count))
    log.write("Total run time: {} seconds\n".format(time.perf_counter() - start_time))


if __name__ == '__main__':
    main()
