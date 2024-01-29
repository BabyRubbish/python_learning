from pathlib import Path

path = Path("cats.txt")
try:
    contents_0 = path.read_text()
except FileNotFoundError:
    print("The file isn't exist!")
else:
    print(contents_0)

path = Path("dogs.txt")
try:
    contents_1 = path.read_text()
except FileNotFoundError:
    print("The file isn't exist!")
else:
    print(contents_1)
