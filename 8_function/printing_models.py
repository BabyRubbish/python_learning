# 首先创建一个列表,其中包含一些要打印的设计
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# 模拟打印每个设计,知道没有未打印的设计为止
# 打印每个设计后,都将器一到列表 completed_models 中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# 显示已经打印好的所有模型
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)
