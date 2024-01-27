import pizza
from pizza import make_pizza
from pizza import make_pizza as mp
import pizza as p
from pizza import *

pizza.make_pizza(16, "pepperni")
pizza.make_pizza(
    12,
    "mushroom",
    "green pepper",
    "extra chesse",
)

make_pizza(16, "pepperni")
make_pizza(
    12,
    "mushroom",
    "green pepper",
    "extra chesse",
)

mp(16, "pepperni")
mp(
    12,
    "mushroom",
    "green pepper",
    "extra chesse",
)

p.make_pizza(16, "pepperni")
p.make_pizza(
    12,
    "mushroom",
    "green pepper",
    "extra chesse",
)
