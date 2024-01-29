from pathlib import Path


def count_word(path):
    """计算一个文件大致包含多少个单词"""
    try:
        contents = path.read_text(encoding="Utf-8")
    except FileNotFoundError:
        # print(f"The file {path} does not exist.")
        # 静默失败
        pass
    else:
        # 计算文件大致包含多少单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")


# path = Path("alice.txt")
# count_word(path)
filenames = [
    "alice.txt",
    "siddhartha.txt",
    "moby_dick.txt",
    "little_women.txt",
]

for filename in filenames:
    path = Path(filename)
    count_word(path)
