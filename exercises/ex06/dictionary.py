"""Dictionary."""

__author__ = "730684472"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Inverts any dict of strings."""
    dict_2: dict[str, str] = {}  # lines 8-11 create variables
    list_2: list[str] = list()
    idx: int = 0
    counter: int = 0
    for key in dict_1:  # for key values in input dict
        list_2.append(dict_1[key])  # append input key to list
        if (list_2[counter] == list_2[idx] and counter != idx):  # if list has two matching values that are not themselfs
            raise KeyError("Two matching keys.")  # raise keyerror
        idx += 1  # counter add
    for key in dict_1:  # for key in input dict
        value: str = dict_1[key]  # value equals input key
        dict_2[value] = key  # output dict key equals input key
    return dict_2  # return output dict


def favorite_color(dict_1: dict[str, str]) -> str:
    """Function that finds the most popular color in a dict."""
    dict_2: dict[str, int] = {}  # lines 25-28 create variables
    top_color: str = ""
    color_freq: int = 0

    for key in dict_1:  # for keys in input dict
        dict_1[key] = dict_1[key].lower()
        if (dict_1[key] in dict_2):  # if input key is in output dict
            dict_2[dict_1[key]] += 1  # add counter
        else:  # if not
            dict_2[dict_1[key]] = 1  # create counter
    for color in dict_2:  # for ints in output dict
        if (dict_2[color] > color_freq):  # if dict int is greater then color_freq
            color_freq = dict_2[color]  # color freq equals dict int
            top_color = color  # top color now equals color for the next run
    return top_color
    

def count(list_1: list[str]) -> dict[str, int]:
    """Function that counts the amount of time each string appears in a list."""
    dict_1: dict[str, int] = {}  # creating output dict
    for elem in list_1:  # for elements in list
        if (elem in dict_1):  # if element is in output dict
            dict_1[elem] += 1  # output dict +=1 
        else:  # if not
            dict_1[elem] = 1  # create new elem with value 1
    return dict_1  # output dict 


def alphabetizer(list_1: list[str]) -> dict[str, list[str]]:
    """Function will alphabetize a list of strings."""
    dict_1: dict[str, list[str]] = {}  # creating output dict
    idx: int = 0
    for elem in list_1:  # for elements in list
        elem = elem.lower()  # lowers all uppercase letters
        if (elem[0] in dict_1):  # if element in dict
            dict_1[elem[0]].append(elem)  # add element to list
        else:  # else
            dict_1[elem[0]] = [elem]  # creates new dict key with element 
    return dict_1  # return dict 


def update_attendance(dict_1: dict[str, list[str]], day: str, stud: str) -> dict[str, list[str]]:
    """Function updates a attendance roster."""
    if (day in dict_1):  # if the day is in the input dict
        dict_1[day].append(stud)  # add student to that day 
    else:  # else
        dict_1[day] = [stud]  # create the day with value of student 
    return dict_1