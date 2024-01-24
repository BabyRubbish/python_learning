my_foods = ["pizza", "falafel", "carrot cake"]

# 这是行不通的
# 这相当于C++中将两个指针指向同一个数组
friend_foods = my_foods

my_foods.append("cookie")
my_foods.append("ice cream")
print(my_foods)
print(friend_foods)

print("\nThe first three items in the list are：")
print(my_foods[0:3])

print("\nThree items from the middle of the list are:")
print(my_foods[1:4])

print("\nThe last three items in the list are：")
print(my_foods[-3:])
