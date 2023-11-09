"""Instantiaing a Class."""

"""
This is where we instantiate the class we defined in classes.py
In other wods, we are creating objects that belong to that class
"""

#import the class 
#from <file_name>,<module_name import <class_name>
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("small",5,True) #CONSTRUCTOR

#accesing/settings attributes 
#my_pizza.size = "large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True 

#print out some values
#print("my_pizza: ")
#print(my_pizza)

#print("Pizza:")
#print(Pizza)

#print("Size Attributes:")
#print(my_pizza.size)

#print("Toppings:")
#print(my_pizza.toppings)

#sals_pizza size "medium, 5 toppings, NOT GF 
sals_pizza: Pizza = Pizza("medium", 5, False)

def price(input_pizza: Pizza) ->float:
    """Calculate Pirce of Pizza"""
    if (input_pizza.size == "large"):
        price: float = 6.25
    else:
        price:float = 5.00
    price += .75 * input_pizza.toppings
    if(input_pizza.gluten_free):
        price += 1.00
    return price

#calling price function
print(price(sals_pizza))
print(price(my_pizza))

# calling price method
print(sals_pizza.price())
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(2)
print(my_other_pizza.toppings)
print(my_pizza.toppings)

