alien_0 = {"color": "green", "point": 5}
alien_1 = {"color": "yellow", "point": 10}
alien_2 = {"color": "red", "point": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 创建一个用于储存外星人的空列表
aliens = []

# 创建30个绿色的外星人
# python认为这三十个特征相同的外星人是独立的
for alien_number in range(30):
    new_alien = {"color": "green", "point": 5, "speed": "slow"}
    aliens.append(new_alien)

# 改变前面3个外星人
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] == "red"
        alien["point"] = 15
        alien["speed"] = "fast"

for alien in aliens[:5]:
    print(alien)

print("···")

# 显示创建了多少个外星人
print(f"Total number of aliens: {len(aliens)}")
