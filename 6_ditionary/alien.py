alien_0 = {
    "color": "green",
    "points": 5,
}
print(alien_0["color"])
print(alien_0["points"])

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

alien_1 = {}
alien_1["color"] = "red"
alien_1["point"] = "5"
print(alien_1)

alien_2 = {
    "color": "green",
}
print(f"The alien is is {alien_2['color']}.")
alien_2["color"] = "yellow"
print(f"The alien is now {alien_2['color']}.")
