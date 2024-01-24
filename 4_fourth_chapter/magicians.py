magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    # python在使用print()函数后会自动换行，\n相当于空出一行
    print(f"I can't wait to see you next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

# python中没有作用域的限制
print(magician.title())
