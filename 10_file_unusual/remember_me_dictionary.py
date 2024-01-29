from pathlib import Path
import json


def get_stored_info(path):
    """如果用户存储了用户名,就获取它"""
    if path.exists():
        contents = path.read_text()
        # print(contents) 得到 "Eric",而不是 Eric
        # json.loads()	将Json字符串解码成python对象
        userinfo = json.loads(contents)
        return userinfo
    else:
        return None


def greet_user():
    """问候用户,并且指出其名字"""
    path = Path("user_info_dictionary.json")
    user_name = get_stored_info(path)
    if user_name["name"] == input("What's your name?"):
        print(f"Welcom back, {user_name['name'].title()}!")
        for info, contents in user_name.items():
            if info == "name":
                continue
            print(f"{info.title()}: {contents.title()}")
    else:
        user_info_dictionary = {}
        user_name = input("What is your name? ")
        user_info_dictionary["name"] = user_name
        user_age = input("How old are you? ")
        user_info_dictionary["age"] = user_age
        user_location = input("Where are you from? ")
        user_info_dictionary["location"] = user_location
        contents = json.dumps(user_info_dictionary)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {user_name.title()}!")


greet_user()
