"""Guess a number (conditional practice)"""
"""Spiese, Thomas"""


my_number_string: str = input("Guess a number: ")
my_number: int = int(my_number_string)

if my_number == 10:
    print("You guessed the right number")
else:
    print("You guessed the wrong number, try again. :(")
    

