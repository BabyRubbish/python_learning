user_names = ["admin", "jhon", "jaden", "tom", "amy"]

for user_name in user_names:
    if user_name == "admin":
        print("Hello admin, would you like to see a status report.")
    else:
        print(f"Hello {user_name.title()}, thank you for logging in again.")

for index in range(len(user_names)):
    user_names.pop()

if user_names:
    print(user_names)
else:
    print("\nWe need to find some users.")
