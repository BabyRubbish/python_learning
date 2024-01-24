favorite_place = {
    "amy": ["nan_jing", "bei_jing", "guanh_zhou"],
    "mike": ["guang_zhou", "shang_hai"],
    "jhon": ["hai_nan"],
}
for person, places in favorite_place.items():
    if len(places) > 1:
        print(f"{person.title()} has {len(places)} favorite places:")
        for place in places:
            print(place.title())
    else:
        print(f"{person.title()}'favorite place is {place.title()}.")
