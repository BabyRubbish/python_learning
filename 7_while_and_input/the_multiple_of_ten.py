prompt = "Please input a number, I will tell you if it is the multiple of ten: "
number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(f"The {number} is a multiple of ten.")
else:
    print(f"The {number} isn't a multiple of ten.")
