def describe_city(city, country="China"):
    """Describe the city in which country."""
    print(f"{city.title()} is in {country.title()}.")


describe_city("shanghai")
describe_city("beijing")
describe_city("new york", "america")


def city_country(city, country):
    combination = f"{city.title()}, {country.title()}"
    return combination


city_country_stage = []
city_country_stage.append(city_country("shanghai", "china"))
city_country_stage.append(city_country("new york", "america"))
city_country_stage.append(city_country("london", "british"))

for stage in city_country_stage:
    print(stage)
