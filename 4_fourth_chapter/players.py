players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print(players[1:4])
print("\n")

print(players[:4])
print(players[1:])
print("\n")

print(players[-2:])
print(players[:-2])
print("\n")

print(players[0:5:2])
print("\n")

print("Here are the first players on my team.")
for player in players[0:3]:
    print(player)
