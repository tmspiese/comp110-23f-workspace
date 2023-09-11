"""EX - 01 Chardle - A step towards Wordle"""

__author__ = "730684472"


user_word: str = input("Enter a 5-character word: ") #Setting variables and user input for said variables 
user_guess: str = input("Please Enter a single character: ") #Setting variables and user input for said variables
total_instance: int = 0 #Counter for total instances of the letter in the word

print("Searching for " + user_guess + " in " + user_word) #indicates to user that search is happening incase of crash

if(len(user_word) != 5): #Need to evaluate to make sure the word has 5 characters and gives appropriate response if not
   print("Error: Word must contain 5 characters.")
   exit()

if(len(user_guess) != 1): #Need to evaluate to make sure the guess is 1 character and gives appropriate response if not 
    print("Error: Character must be a single character.")
    exit()

if(user_word[0] == user_guess):  #These are if statments to both compare each letter in the word and the character
    print(user_guess + " found at index 0")# and count how many instances of that letter occur (lines 20-34)
    total_instance += 1
if(user_word[1] == user_guess):
    print(user_guess + " found at index 1")
    total_instance += 1
if(user_word[2] == user_guess):
    print(user_guess + " found at index 2")
    total_instance += 1
if(user_word[3] == user_guess):
    print(user_guess + " found at index 3")
    total_instance += 1
if(user_word[4] == user_guess):
    print(user_guess + " found at index 4")
    total_instance += 1

if(total_instance > 0): #Print to user the number of instances the letter occur in the word 
    print(str(total_instance) + " instances of " + user_guess + " found in " + user_word)
else: #If the letter occures 0 times this will be printed 
    print("No instances of "+ user_guess + " was found in " + user_word)