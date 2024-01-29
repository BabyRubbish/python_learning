from pathlib import Path

guest_book = ""
while True:
    print("Please input the name:")
    name = input("(Enter 'q' at any time to quit)")
    if name == "q":
        break
    name += "\n"
    guest_book += name
path = Path("guest_book")
path.write_text(guest_book)
