pet_0 = {
    "kind": "cat",
    "owner": "amy",
    "age": 2,
}
pet_1 = {
    "kind": "dog",
    "owner": "mike",
    "age": 3,
}

pet_2 = {
    "kind": "turtle",
    "owner": "jhon",
    "age": 10,
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"{pet['owner'].title()}'s pet is a {pet['kind']}.")
    print(f"And it is {pet['age']} years old.")
