"""
相当于C++中：
for(int i = 1, i < 5, i++)
{
    cout << i <<endl;
}
"""

for value in range(1, 5):
    print(value)

# 使用 list() 函数将 range(1,6) 产生的数字转换为列表(list)
numbers = list(range(1, 6))
print(numbers)
