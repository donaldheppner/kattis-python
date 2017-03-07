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
    recipes = list()
    for recipe_number in range(0, number_of_recipes):
        recipes.append({map(int, input.readline().split()[1:])})

    recipe_count = 0
    cauldrons = list() # mixed recipes
    used_ingredients = set()

    for recipe in recipes:
        if recipe not in used_ingredients:
            cauldrons.append(recipe)    # record the cauldron
            used_ingredients |= recipe  # note the used ingredients, union sets
            recipe_count += 1
        else: # can I combine cauldrons?
            candidate_cauldrons = list()
            for cauldron in cauldrons:
                remaining_ingredients = recipe.copy()
                if cauldron <= recipe:
                    candidate_cauldrons.append(cauldron)
                    remaining_ingredients -= cauldron
                    if remaining_ingredients not in used_ingredients:
                        # success! mix the ingredients and record the new cauldron
                        used_ingredients |= remaining_ingredients
                        new_cauldron = remaining_ingredients
                        for c in candidate_cauldrons:
                            cauldrons.remove()
                            new_cauldron |= c
                        cauldrons.append(c)
                        recipe_count += 1
                        break

    output.write("{}".format(recipe_count))


if __name__ == '__main__':
    main()
