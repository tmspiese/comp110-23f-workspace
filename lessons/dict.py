"""Practice with Dictionaries"""

ice_cream: dict[int, str]={1: "Chocolate", 2: "Vanilla", 3: "Strawberry"}
print("Made my dictionary.")
print(ice_cream)
ice_cream[4] = "Mint"
print("Added key, value pair to dictionary")
print(ice_cream)
ice_cream.pop(3)
print("Removing key 3 from dict")
print(ice_cream)
print("Changing key 1 from chocolote to Mint")
ice_cream[1] = "Strawberry"
print(ice_cream)


