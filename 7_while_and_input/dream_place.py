prompt_0 = "What's you name? "
prompt_1 = "If you could visit one place in the world, where would you go? "
prompt_2 = "Would you like to let another people to respond?(yes/no)"
dream_places = {}
polling_active = True
while polling_active:
    # 获取被采访者的姓名
    name = input(prompt_0)
    # 获取被采访者的回答
    dream_place = input(prompt_1)

    # 存储被采访者的信息及其回答
    dream_places[name] = dream_place

    # 询问是否还有其他人参与
    repeat = input(prompt_2)
    if repeat == "no":
        polling_active = False

print("---Poll Results---")
for name, place in dream_places.items():
    print(f"{name.title()}'s dream place is {place.title()}!")
