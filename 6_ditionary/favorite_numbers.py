# favorite_numbers = {
#     "Jhon": 18,
#     "Amy": 5,
#     "Sarah": 8,
#     "Mike": 7,
#     "Rose": 6,
# }
# print("My friends' favorite numbers are:")
# for favorite_number in favorite_numbers:
#     print(f"{favorite_number}:{favorite_numbers[favorite_number]}")
favorite_numbers = {
    "Jhon": [18, 87],
    "Amy": [5, 4],
    "Sarah": [8, 85],
    "Mike": [7, 89],
    "Rose": [6, 25],
}
for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are as follow:", end=" ")
    for number in numbers:
        print(f"{number}", end=" ")
        if number == numbers[len(numbers) - 1]:
            print("")
