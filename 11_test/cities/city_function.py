def city_country(city, country, population=""):
    """返回一个 City, Country 字符串"""
    if population:
        combination = f"{city}, {country} - population {population}"
    else:
        combination = f"{city}, {country}"
    return combination.title()
