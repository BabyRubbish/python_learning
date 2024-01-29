# 调用pathlib
from pathlib import Path

path = Path("pi_digital.txt")
contents = path.read_text()
contents = contents.strip()
print(contents)
print("")

lines = contents.splitlines()
for line in lines:
    print(line)
