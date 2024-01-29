print("Give me two numbers, and I'll add them.")
print("Enter 'q' at any time to quit.")

while True:
    first_number = input("First number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter a number!")
    else:
        print(answer)
