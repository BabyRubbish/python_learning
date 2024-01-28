# 只导入ElectricityCar
from electric_car import ElectricCar
from car import Car

# 导入所有,但是需要用car.class_name访问
import car

# 导入所有,但是不需要用car.class_name访问
from car import *

my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_describe_name())
my_new_car.update_odometer(5)
my_new_car.odometer_reading = 23
my_new_car.update_odometer(50)
my_new_car.increment_odometer(50)
my_new_car.read_odometer()


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_describe_name())
my_leaf.battery.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
