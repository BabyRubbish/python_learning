from random import randint

lottery = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "G",
    "F",
    "S",
    "W",
    "X",
]


def get_lottery(lottery):
    """随机选出四位数字和字母的组合"""
    outcome = ""
    for i in range(0, 4):
        outcome += lottery[randint(0, len(lottery)) - 1]
    return outcome


luck_lottery = "482G"
print(f"If you get {luck_lottery}, you will get a great award!")
count = 0
while True:
    my_lottery = get_lottery(lottery)
    print(f"My lottery is {my_lottery}.")
    count += 1
    if my_lottery == luck_lottery:
        print("A great award!")
        print(f"You have bought the lottery for {count} times!")
        break
