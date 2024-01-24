rivers = {
    "nile": "egypt",
    "yangtse river": "china",
    "messissippi": "america",
}
print(f"The {list(rivers.keys())[0].title()} " "runs through {rivers['nile'].title()}.")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
