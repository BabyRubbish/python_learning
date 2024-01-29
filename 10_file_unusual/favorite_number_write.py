from pathlib import Path
import json

path = Path("favorite_number.json")
contents = input("What's you favorite number?")
contents = json.dumps(contents)
path.write_text(contents)
print(f"We'll print it, when you come back.")
