# int()利用类型转换实现string变成int型
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
