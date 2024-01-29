from pathlib import Path
import json

path = Path("username.json")
if path.exists():
    contents = path.read_text()
    # print(contents) 得到 "Eric",而不是 Eric
    # json.loads()	将Json字符串解码成python对象
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What's your name?")
    # 将名字储存到json中
    # json.dumps()	将python对象编码成Json字符串
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}")
