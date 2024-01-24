# 字典分行定义必须要在每一对键值后面加上逗号，否则会变成一行
favorite_languages = {
    "jen": "python",
    "sarah": "C",
    "edward": "rust",
    "phli": "python",
}

language = favorite_languages["sarah"].title()
print(f"Sarah's favorite langue is {language}.\n")

# 利用items()函数和for循环实现对字典的遍历
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language}.")

# 使用keys()可以获得字典中的键名
# 该句等价于for name in favorite_languages：
for name in favorite_languages.keys():
    print(name.title())

friends = {
    "sarah",
    "phli",
}

for name in favorite_languages.keys():
    print(f"Hi,{name}")
    if name in friends:
        print(f"\t{name.title()}, I see you love {favorite_languages[name]}!")

if "erin" not in favorite_languages:
    print("Erin, please take our poll.")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()},thank you for taking the poll.")

print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())
print()

print("The following languages have been mentioned: ")
# 可以利用set集合来进行舍弃重复元素
for language in set(favorite_languages.values()):
    print(language.title())

# 可以利用花括号直接定义集合
languages = set(favorite_languages.values())
print(languages)

languagess = {
    "C",
    "python",
    "rust",
    "python",
}
print(languagess)
