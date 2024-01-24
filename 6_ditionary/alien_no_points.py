alien_0 = {
    "color": "green",
    "speed": "slow",
}
# print(alien_0["points"])
# 利用get()来使得指定的键不存在时返回一个默认值
point_value = alien_0.get("points", "No point value assigned.")
print(point_value)
