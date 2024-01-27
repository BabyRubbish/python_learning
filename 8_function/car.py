def make_cars(brand, model, **car_info):
    """将一辆汽车的信息存储在字典中"""
    car_info["brand"] = brand
    car_info["model"] = model
    return car_info


car = make_cars(
    "subaru",
    "outback",
    color="black",
    tow_package=True,
)
print(car)
