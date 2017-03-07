import sys
import time
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

        used_remaining_ingredients = list(recipe & used_ingredients)
        heapq.heapify(used_remaining_ingredients)

        if is_target_recipe:
            log.write("used_remaining_ingredients union: {} seconds\n".format(time.perf_counter() - comp_time))

        # if no used ingredients and recipe is just one ingredient, consider it unused (got us to 19/40)
        if len(used_remaining_ingredients) == 0:
            if len(recipe) == 1:
                concocted_count += 1
                continue
            else:
                # no used remaining ingredients, just add the recipe and continue
                ingredient_cauldrons[min(recipe)] = recipe
                used_ingredients |= recipe
                concocted_count += 1
                continue

        total_set_add_time = 0.0
        total_set_intersection_time = 0.0
        total_subset_time = 0.0
        total_cauldron_get_time = 0.0

        first_ingredients = set()
        mixed_ingredients = set()
        while len(used_remaining_ingredients) != 0:
            # TIMED BLOCK START: cauldron get time
            if is_target_recipe:
                cauldron_get_time = time.perf_counter()
            # get the next first ingredient
            while len(used_remaining_ingredients) > 0:
                first_ingredient = heapq.heappop(used_remaining_ingredients)
                if first_ingredient not in mixed_ingredients:
                    break
            else:
                continue   # all done with used ingredients, this will run the else clause of the while loop
            # first_ingredient = used_remaining_ingredients.pop()                  # timed line: SLOW (faster now with sorted set ... sorted set not supported by kattis, going to heapq)
            if is_target_recipe:
                total_cauldron_get_time += (time.perf_counter() - cauldron_get_time)
            # TIMED BLOCK END
            candidate_cauldron = ingredient_cauldrons.get(first_ingredient)
            if candidate_cauldron is not None:
                # TIMED BLOCK START: set subset time
                if is_target_recipe:
                    set_subset_time = time.perf_counter()
                is_subset = candidate_cauldron <= recipe                        # timed line
                if is_target_recipe:
                    total_subset_time += (time.perf_counter() - set_subset_time)
                # TIMED BLOCK END
                if is_subset:
                    # TIMED BLOCK START: set intersection
                    if is_target_recipe:
                        set_intersection_time = time.perf_counter()
                    mixed_ingredients |= candidate_cauldron                     # store the ingredients we've mixed, this will help with popping from the heapq
                    if is_target_recipe:
                        total_set_intersection_time += time.perf_counter() - set_intersection_time
                    # TIMED BLOCK END

                    # TIMED BLOCK START: set add
                    if is_target_recipe:
                        set_add_time = time.perf_counter()
                    first_ingredients.add(first_ingredient)                     # timed line
                    if is_target_recipe:
                        total_set_add_time += time.perf_counter() - set_add_time
                    # TIMED BLOCK END
                else:
                    # can't make it work, the cauldron isn't a subset of the recipe
                    break
            else:
                # can't make it work, none of our cauldrons have a matching first ingredient
                break
        else:
            # TIMED BLOCK START: clean-up
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
            # TIMED BLOCK END

    if is_target_problem:
        log.write("Total set intersection time: {} seconds\n".format(total_set_intersection_time))
        log.write("Total set add time: {} seconds\n".format(total_set_add_time))
        log.write("Total set subset time: {} seconds\n".format(total_subset_time))
        log.write("Total cauldron get time: {} seconds\n".format(total_cauldron_get_time))

    output.write("{}".format(concocted_count))
    log.write("Total run time: {} seconds\n".format(time.perf_counter() - start_time))


if __name__ == '__main__':
    main()
