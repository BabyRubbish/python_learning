prompt = "Could you tell me your age, so that I can offer you the fee? "
prompt += "\nEnter 'quit' to quit.    "
active = True
while active:
    age = input(prompt)
    if age == "quit":
        active = False
    elif int(age) < 3:
        print("It's free.")
    elif 3 <= int(age) <= 12:
        print("The price is 10$.")
    else:
        print("The price is 15$.")
