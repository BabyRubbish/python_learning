# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ["alice", "brain", "canace"]
confirmed_users = []

# 验证每个用户，知道没有未验证的用户为止
# 将每个经过验证的用户都移动到已经验证的用户列表中
while unconfirmed_users:
    # 接收每一个未验证的用户
    current_user = unconfirmed_users.pop()
    # 打印正在验证的用户
    print(f"Varifying user: {current_user.title()}")
    # 将已经验证的用户加入到已经验证的用户列表中
    confirmed_users.append(current_user)

# 显示所有已经验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
