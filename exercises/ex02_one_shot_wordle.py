"""EX - 02 - One Shot Wordle."""

__author__ = "730684472"

secret_word: str = "python"

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

anywhere_in_guess: bool = False  

player_anwser: str = ""
counter_1: int = 0
counter_2: int = 0

user_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")  # base user input for there guess 

while (len(user_guess) != len(secret_word)):  # need to evaluate to make sure the word has 6 characters and gives appropriate response if not
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")  # print to user that the input was no valid and to try again and get new input

while (len(secret_word) != counter_1):  # while the secret word (6 right now) is less then the counter (so we can test each character) do below
    if (secret_word[counter_1] == user_guess[counter_1]):  # if user guess character equals the secret word character 
        player_anwser = player_anwser + green_box  # save green box in output value and repeat for next character 
    elif (secret_word[counter_1] != user_guess[counter_1]):
        while (anywhere_in_guess is False) and (counter_2 < len(secret_word)):  # while its nowhere in the string so far evaluated and the secondary counter is less then the length of the secret word do following
            if (str(secret_word[counter_2]) == str(user_guess[counter_1])):  # if the chosen character of the secret word equals the character of the users guesses character
                anywhere_in_guess = True  # make the boolean statement that the users character is somewhere within the secret word True 
            else:  # if still flase
                counter_2 = counter_2 + 1  # increase the secondary counter by one so the next character within the users guess can be compared to the same character within the secret word
    if (anywhere_in_guess is True):  # if the users character is somewhere within the secret word
        player_anwser = player_anwser + yellow_box  # put a yellow box in that place 
    elif (secret_word[counter_1] != user_guess[counter_1]):  # if the users character is not anywhere with the secret word and the character of the secret word is not the character of the users guess
        player_anwser = player_anwser + white_box  # put a white box in that place
    counter_1 = counter_1 + 1  # increase primary counter by one so the while loop can reevauate 
print(player_anwser)

if (user_guess == secret_word):  # Compare the users guess to the secret word
    print("Woo! You got it!")  # They guessed the right word. WOW
else: 
    print("Not quite. Play again soon!")  # They didn't guess the right word
