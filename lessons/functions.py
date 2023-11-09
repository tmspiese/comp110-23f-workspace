"""Demonstrates functions and syntax"""

number_1: int 
Number_2: int

def my_max(number_1, number_2) -> int:
    """Returns the maximum value ut of 2 numbers"""
    if( number_1>= number_2):
        return number_1
    else: # number 1 < number 2
        return number_2


max_number: int = my_max(1, 10)
other_max_number: int = my_max(11,3)
print(other_max_number)



def my_max(number_1: int, number_2: int) -> int:
    """Returns the maximum value ut of 2 numbers"""
    if( number_1>= number_2):
        return number_1
    else: # number 1 < number 2
        return number_2


max_number: int = my_max(1, 10)
other_max_number: int = my_max(11,3)
print(other_max_number)

