from pathlib import Path
import json


def get_stored_numbers(path) -> Path:
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        return favorite_number
    else:
        return None


def tell_user():
    path = Path("favorite_number.json")
    favorite_number = get_stored_numbers(path)
    if favorite_number:
        print(f"I konw your favorite number! It's {favorite_number}.")
    else:
        while True:
            contents = input("What's you favorite number? ")
            try:
                contents == int(contents)
                break
            except ValueError:
                print("Please enter again!")

        contents = json.dumps(contents)
        path.write_text(contents)
        print(f"We'll print it, when you come back.")


tell_user()
