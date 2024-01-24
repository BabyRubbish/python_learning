mo_yusen = {
    "first_name": "Mo",
    "last_name": "Yusen",
    "age": 19,
    "city": "nanjing",
}

zhang_huaiwen = {
    "first_name": "zhang",
    "last_name": "huaiwen",
    "age": 19,
    "city": "tianjing",
}

sun_yeqi = {
    "first_name": "sun",
    "last_name": "yeqi",
    "age": 19,
    "city": "taizhou",
}

people = [
    mo_yusen,
    zhang_huaiwen,
    sun_yeqi,
]

for person in people:
    first_name = person["first_name"]
    last_name = person["last_name"]
    age = person["age"]
    city = person["city"]
    name = first_name + last_name
    print(f"The infomation of {name.title()} are: ")
    print(f"Name:{first_name.title()} {last_name.title()}")
    print(f"Age: {age}")
    print(f"City: {city.title()}")
