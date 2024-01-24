# 存储顾客所点的pizza信息
pizza = {
    "crust": "thick",
    "topping": ["mushrooms", "extra cheese"],
}

# 概述顾客点的的pizza
print(f"You ordered a {pizza['crust']}-crust pizza " "with the folowing topping.")

for topping in pizza["topping"]:
    print(f"\t{topping}")
