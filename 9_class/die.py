from random import randint


class Die:
    """一个骰子类"""

    def __init__(self, sides=6) -> None | int:
        """初始化骰子属性"""
        self.sides = sides

    def roll_die(self):
        self.outcome = randint(1, self.sides)
        print(f"This time you get {self.outcome}.")


sides = [6, 10, 20]
for side in sides:
    my_die = Die(sides=side)
    count = 0
    while True:
        my_die.roll_die()
        count += 1
        if count == 10:
            break
