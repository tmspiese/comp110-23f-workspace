"""Practice importing from other modules"""

from lessons import my_functions

if( __name__ == "__main__"):
    print("Howdy!")

def f(x:int) -> int:
    return(x)
    x *= 2
    print (x)

y:int = f(3)

print(y)