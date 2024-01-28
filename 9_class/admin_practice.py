from admin import Admin

baby_rubbish = Admin(
    "baby",
    "rubbish",
    "can add post",
    "can delete post",
    favorite_coloe="blue",
    location="nanjing",
)

baby_rubbish.describe_user()
baby_rubbish.privileges.show_privileges()
