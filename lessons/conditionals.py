"""Testing Conitionals with low card exmaples"""
"""Spiese, Thomas"""

low_card: int=2
current_card: int=3

if current_card<low_card:
    low_card = current_card
else:
    print(str(current_card) + " is not the lowest card")
print("The lowest card is " + str(low_card))