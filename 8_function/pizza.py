def make_pizza(size, *toppings):
    # toppings 是一个元组
    """打印顾客点的所有配料"""
    print(f"\nMaking a {size}-inch pizza with the folowing toppings:")
    for topping in toppings:
        print(f"-{topping}")
