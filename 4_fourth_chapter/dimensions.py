dimensions = (200, 20)

print(dimensions[0])
print(dimensions[1])

#'tuple' object does not support item assignment
# dimensions[0] = 20

# 只有一个元素的元组也需要加逗号
my_t = (1,)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (500, 40)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
