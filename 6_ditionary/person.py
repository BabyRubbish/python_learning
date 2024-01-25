mo_yusen = {
    "first_name": "Yusen",
    "last_name": "Mo",
    "age": 19,
    "city": "nanjing",
}

zhang_huaiwen = {
    "first_name": "huaiwen",
    "last_name": "zhang",
    "age": 19,
    "city": "tianjing",
}

sun_yeqi = {
    "first_name": "yeqi",
    "last_name": "sun",
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
