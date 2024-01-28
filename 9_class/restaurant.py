class Restaurant:
    """一次模拟餐厅的尝试"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始描述餐厅的性质"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_severed = 0

    def describe_restaurant(self):
        """打印出餐厅的名字和菜肴类型"""
        print(f"The name of the restaurant: {self.restaurant_name}")
        print(f"The cuisin type is {self.cuisine_type}.")

    def open_restuarant(self):
        """餐厅营业"""
        self.state = True
        print(f"The restaurant is opening!")

    def show_number_severed(self):
        print(f"The number the restaurant has severed is {self.number_severed}.")

    def set_number_served(self, new_number):
        self.number_severed = new_number

    def increment_number_served(self, growth):
        self.number_severed += growth


# restaurant = Restaurant("Cool", "Chinese Food")
# restaurant.describe_restaurant()
# restaurant.open_restuarant()

# restaurant_1 = Restaurant("Hot", "Fast Food")
# restaurant_1.describe_restaurant()

# restaurant_2 = Restaurant("Cold", "BBQ")
# restaurant_2.describe_restaurant()

# restaurant.show_number_severed()
# restaurant.number_severed = 50
# restaurant.show_number_severed()
# restaurant.set_number_served(100)
# restaurant.show_number_severed()
# restaurant.increment_number_served(200)
# restaurant.show_number_severed()
