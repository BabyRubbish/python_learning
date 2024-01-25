pets = ["dog", "cat", "dog", "dog", "goldfish", "cat", "rabbit", "cat"]

print(pets)

while "cat" and "dog" in pets:
    pets.remove("dog")
    pets.remove("cat")
print(pets)
