"""Combining two lists inot a dictionary."""


__author__ = "730684472"


def zip(list_1: list[str], ints: list[int]) -> dict[str, int]:
    """Creating a function that takes 2 lists and puts them into one dict."""
    idx: int = 0  # counter declaration
    Combine: dict[str, int] = {}  # declaration of dict
    if (len(list_1) != len(ints)):  # making sure lists are equal, if not exit()
        return {}
    
    while (len(list_1) > idx and len(ints) > idx):  # lists are longer then the index counter 
        key: str = list_1[idx]  # key of dict = list_1[counter]
        value: int = ints[idx]  # value of dict = ints[counter]
        Combine[key] = value  # adding new key, value pair to dict
        idx = idx + 1  # counter increases by one
        
    return Combine  # return dict
     

    



        
