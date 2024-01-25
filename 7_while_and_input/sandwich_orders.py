print(f"All the pastrami are sold!")
sandwich_orders = {
    "simple sanwich",
    "steak sanwich",
    "pastrami",
    "panini sanwich",
    "pastrami",
    "tuna sanwich",
    "pastrami",
}
finished_sandwich = []

print(sandwich_orders)
# 删除所有的pastrami
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)

for sanwich in sandwich_orders:
    print(f"I made you {sanwich}")
    finished_sandwich.append(sanwich)
print(f"The following sanwiches are finished!")
for sanwich in finished_sandwich:
    print(sanwich.title(), end="  ")
