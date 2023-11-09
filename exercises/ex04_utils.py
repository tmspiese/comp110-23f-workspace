"""EX-04 Utils."""

__author__ = "730684472"


def all(user_input: list[int], check_int: int) -> bool:
    """Tells us if a list of intergers is equal to a single interger."""
    ind: int = 0  # defining a ind
    while (0 <= len(user_input)):  # while the length of the list is list than or equal to 0
        if (len(user_input) == 0):  # if the length of the list equals zerp
            return False  # return false
        if (user_input[ind] == check_int):  # if one int within the list equals the single interger
            ind = ind + 1  # ind will increase by one to test the next number in the list
        else:  # if the interger within the list does not equal the 
            return False  # return false
        if (ind == len(user_input)):  # if the ind equals the length of the list 
            return True  # return true
    return False
 

def max(inputs: list[int]) -> int:
    """Tells us what the max interger is within a given list."""
    if (len(inputs) == 0):  # if length of list equals zero 
        raise ValueError("max() arg is an empty List")  # shoot back a error
    
    ind: int = 0  # declaration
    high_int: int = inputs[0]  # declaration
    while (len(inputs) > ind):  # while the length of the list i greater then the ind
        if (high_int <= inputs[ind]):  # if the highest int so far in the list is less than or equal too this 
            high_int = inputs[ind]  # highest int equals that 
        ind = ind + 1  # counter ++
    return high_int  # return highest integer


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Compares 2 lists of integers and checks to see if they are equal."""
    ind: int = 0  # declaration
    if (len(list_1) != len(list_2)):  # if they lists lengths are equal return false
        return False
    while (len(list_1) > ind and len(list_2) > ind):  # while both list lengths are greater then the counter
        if (list_1[ind] != list_2[ind]):  # if the position of list one is not equal to the position of list 2
            return False  # return false
        ind = ind + 1  # counter ++
    return True  # return true (this only happens if every number in list one is equal to every numbe rin list 2 and the lists are equal length)
    