from user import User


class Privilege:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """呈现这个管理员的权限"""
        print("The privileges of the administer are:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """模拟管理员"""

    def __init__(self, first_name, last_name, *privileges, **other_infos):
        super().__init__(first_name, last_name, **other_infos)
        """初始管理员属性"""
        self.privileges = Privilege(privileges)


# baby_rubbish = Admin(
#     "baby",
#     "rubbish",
#     "can add post",
#     "can delete post",
#     favorite_coloe="blue",
#     location="nanjing",
# )

# baby_rubbish.describe_user()
# baby_rubbish.privileges.show_privileges()
