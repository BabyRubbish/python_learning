prompt = "What topping would you like to add to the pizza?"
prompt += "\nEnter quit to stop!"

while True:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print(f"Please add {topping} to pizza.")
