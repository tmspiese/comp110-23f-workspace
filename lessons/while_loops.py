"""Demonstrates while loops by finding low value in string"""

cards: str = "5235"

card_index: int = 0
low_card: int = int(cards[0])

# loop at each number in the string 
while(card_index <4):
    # check if current card is less then low card
    current_card: int = int(cards[card_index])
    if(current_card < low_card):
        # update low card to be our current card
        low_card = current_card
    card_index = card_index + 1
print(low_card)