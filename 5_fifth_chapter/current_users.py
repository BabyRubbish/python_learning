current_users = ["luffy", "zoro", "nami", "sanji", "chopper"]
new_users = ["robin", "franky", "bRook", "sANji", "Chopper"]

for new_user in new_users:
    for current_user in current_users:
        if new_user.lower() == current_user:
            exist = 1
        else:
            exist = 0
        if exist == 1:
            break

    if exist == 1:
        print(f"{new_user.title()} has been used, please use another one.")
    elif exist == 0:
        print(f"{new_user.title()} hasn't been used.")
