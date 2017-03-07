recipes = 50000
ingredient_index = 1

with open('3.in', 'w') as f:
    f.write("{}\n".format(recipes))

    for x in range(0, recipes - 1):
        # write a bunch fo two ingredient recipes
        f.write("{} {} {}\n".format(2, ingredient_index, ingredient_index + 1))
        ingredient_index += 2

    # write the recipe with all the ingredients
    f.write("{}".format(ingredient_index))
    for ingredient in range(1, ingredient_index + 1):
        f.write(" {}".format(ingredient))

    f.write("\n")

with open('3.ans', 'w') as f:
    f.write("{}".format(recipes))


