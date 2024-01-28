from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """继承Restaurant类并实现冰淇淋小摊的类"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化冰淇淋小摊"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavors(self, *flavors):
        for flavor in flavors:
            self.flavors.append(flavor)
        print("Finished adding flavor!")

    def show_ice_cream_flavors(self):
        print("Here are the flavors in the stand:")
        for flavor in self.flavors:
            print(f"{flavor} ", end="")


my_ice_cream_stand = IceCreamStand("Cold!", "Ice Cream")
my_ice_cream_stand.add_flavors(
    "Cookie Dough",
    "Chocolate Fudge Brownie",
    "Cherry Garcia",
)
my_ice_cream_stand.show_ice_cream_flavors()
