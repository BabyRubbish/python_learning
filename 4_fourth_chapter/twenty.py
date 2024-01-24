# for value in range(1, 21):
#     print(value)

values = [value for value in range(1, 1000001)]

# for value in values:
#     print(value)

value_max = max(values)
value_min = min(values)

print(f"The maximun number in values is {value_max}")
print(f"The minimun number in values is {value_min}")

values_sum = sum(values)
print(values_sum)

# 4.6
odd_numbers = [number for number in range(1, 20, 2)]
for odd_number in odd_numbers:
    print(odd_number)

# 4.7
three_devided_numbers = [number for number in range(3, 31, 3)]
for three_divided_number in three_devided_numbers:
    print(three_divided_number)

# 4.8
cubic_numbers = [value**3 for value in range(1, 11)]
for cubic_number in cubic_numbers:
    print(cubic_number)
