my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foos are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append("cookie")
friend_foods.append("hamburger")

print("\nMy favorite foos are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\nMy favorite foods are:")
for food in my_foods:
    print(food)
