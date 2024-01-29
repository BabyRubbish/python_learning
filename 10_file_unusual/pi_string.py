from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()

pi_string = ""
for line in contents.splitlines():
    # 组合lines 并且使用lstrip 删除空格
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
