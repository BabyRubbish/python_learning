pizzas = ["bar", "pepperoni", "Chicago-style"]
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really love pizza.")

animals = ["cat", "dog", "tuitle"]
for animal in animals:
    print(animal)

for animal in animals:
    print(f"A {animal} makes a great pet.")

print("Any of these animal would make a great pet.")

friend_pizzas = pizzas[:]
friend_pizzas.append("Italy-style")
print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
