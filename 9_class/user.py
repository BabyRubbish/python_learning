class User:
    """定义一个用户类"""

    def __init__(self, first_name, last_name, **other_infos):
        """对用户进行初始化"""
        self.first_name = first_name
        self.last_name = last_name
        self.other_infos = other_infos
        self.login_attempts = 0

    def describe_user(self):
        """描述用户的基本信息"""
        full_name = f"{self.first_name} {self.last_name}"
        print(full_name.title())
        if self.other_infos:
            for info, content in self.other_infos.items():
                print(f"{info.title()}: {content.title()}")
        print("")

    def increment_login_attempts(self):
        """及那个属性 login_atempts 的值加1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将login_attempts置为0"""
        self.login_attempts = 0

    def print_attempts(self):
        """打印登录次数"""
        print(f"You have tried to login for {self.login_attempts} times!")


# baby_rubbish = User("baby", "rubbish", favorite_coloe="white", age=19)
# baby_rubbish.describe_user()

# tut = User("huaiwen", "zhang", favorite_game="率土之滨", age=19)
# tut.describe_user()
# tut.increment_login_attempts()
# tut.print_attempts()
# tut.reset_login_attempts()
# tut.print_attempts()
