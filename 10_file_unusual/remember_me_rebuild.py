from pathlib import Path
import json


def get_stored_name(path):
    """如果用户存储了用户名,就获取它"""
    if path.exists():
        contents = path.read_text()
        # print(contents) 得到 "Eric",而不是 Eric
        # json.loads()	将Json字符串解码成python对象
        username = json.loads(contents)
        return username
    else:
        return None


def greet_user():
    """问候用户,并且指出其名字"""
    path = Path("username.json")
    username = get_stored_name(path)
    if username:
        print(f"Welcom back, {username}!")
    else:
        username = input("What is your name?")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}")


greet_user()
