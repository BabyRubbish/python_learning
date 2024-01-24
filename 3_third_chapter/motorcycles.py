motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append("honda")
print(motorcycles)

motorcycles.insert(0, "victory")
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# pop()函数弹出最后一个元素
poped_motorcycles = motorcycles.pop()
print(poped_motorcycles)
print(motorcycles)

motorcycles.append("honda")
motorcycles.append("yamaha")
print(motorcycles)
