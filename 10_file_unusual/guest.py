from pathlib import Path


def input_name():
    """提示用户输入名字,并返回一个字符串"""
    name = input("Please input you name:")
    return name


name = input_name()
path = Path("guest.txt")
path.write_text(name)
