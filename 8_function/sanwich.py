def add_ingredient(*ingredients):
    """recieve all the ingredients, and then print them."""
    print("We will add the following ingredient to the sanwich:")
    for ingredient in ingredients:
        for ingredient_ in ingredient:
            print(ingredient_)


ingredients = []
prompt = "Please input all the ingredient you need(one by one): "
prompt += "\n(Enter 'q' at any time to quit!) "
while True:
    ingredient = input(prompt)
    if ingredient == "q":
        break
    ingredients.append(ingredient)

add_ingredient(ingredients)
