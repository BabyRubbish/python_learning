cities = {
    "beijing": {
        "country": "china",
        "population": 20000000,
        "fact": "the capital of China",
    },
    "new york city": {
        "country": "america",
        "population": 8800000,
        "fact": "the biggest city of America",
    },
    "toyko": {
        "country": "japan",
        "population": 13920000,
        "fact": "the capital of Japan",
    },
}

for city, belongings in cities.items():
    print(f"{city.title()} is a city in {belongings['country']}.")
    print(f"There are about {belongings['population']} people living there.")
    print(f"one of the fact about {city.title()} is that ", end="")
    print(f"it is {belongings['fact']}")
