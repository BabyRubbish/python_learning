destinations = ["UK", "USA", "india", "Russia", "HongKong"]
print("\nHere is the orginal list:")
print(destinations)

# sorted 函数按照acsii码的顺序进行排列
print(sorted(destinations))

print("\nHere is the orginal list again:")
print(destinations)

print(sorted(destinations, reverse=True))

print("\nHere is the orginal list again:")
print(destinations)

# reverse()
destinations.reverse()
print(destinations)

destinations.reverse()
print(destinations)

# sort()
print("\nHere is the orginal list again:")
print(destinations)
destinations.sort()
print(destinations)

destinations.sort(reverse=True)
print(destinations)

print(destinations[-1])
