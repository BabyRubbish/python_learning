def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet("hamster", "sniff")
describe_pet("hamster", "scurry")

describe_pet(animal_type="hamster", pet_name="sniff")
describe_pet(pet_name="scurry", animal_type="hamster")
