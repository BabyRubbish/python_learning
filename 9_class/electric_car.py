"""一组可用于表示电动汽车的类"""
from car import Car


class Battery:
    """一次模拟电动汽车电池的尝试"""

    def __init__(self, battery=40):
        """初始化电池的属性"""
        self.battery_size = battery

    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            print("You battery size has upgraded!")

    def get_range(self):
        """打印一条消息,指出电池的续航里程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类的信息"""
        super().__init__(make, model, year)
        self.battery = Battery()

    # 描述电池容量的方法已经在Battery类中定义
    # def describe_battery(self):
    #     """打印一条描述电池容量的消息"""
    #     print(f"This car has a {self.battery_size}-kWh battery.")

    # 方法中的self参数是必要的,在调用方法时会有一个self实参
    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't have a gas tank!")
