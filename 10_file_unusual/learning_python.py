from pathlib import Path

path = Path("learning_python.txt")
# read_text 不需要参数
contents = path.read_text()
contents = contents.strip()
contents = contents.replace("Python", "C")
print(contents)

for line in contents.splitlines():
    print(line)
