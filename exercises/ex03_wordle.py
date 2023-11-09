"""EX-03 Structed Wordle."""

__author__ = "730684472"


def contains_char(searched_thru: str, char: str) -> bool:  # function to check for yellow or white block
    """Yellow Check."""
    ind: int = 0  # counter
    assert len(char) == 1  
    while ((ind - 1) < len(searched_thru)):  # while the ind is less than the length of the searched word by one (so i can return False if there are no matches)
        if (ind == len(searched_thru)):  # if the counter equals the length of the word exit fale becasue there are no matches
            return False  # Return False
        elif (searched_thru[ind] == char):  # elif a character within the word does match a character 
            return True  # return true 
        ind = ind + 1  # Counter add and repeat
    return False
    

def emojified(user_guess: str, secret_word: str) -> str:  # function to create emojies (white, green, and yellow)
    """Codifies the guess into white, yellow, or green squares."""
    white_box: str = "\U00002B1C"  # lines 19-23 are basic declarations
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    output: str = ""
    ind: int = 0

    assert len(user_guess) == len(secret_word)  
    while (ind < len(secret_word)):  # while the counter is less then the length of the secret word
        white_or_yellow: bool = contains_char(secret_word, user_guess[ind])  # string value equals either True of False (False means white, True means yellow)
        if (user_guess[ind] == secret_word[ind]):  # If the guess letter and the secret letter are equal
            output = output + green_box  # Add a green box and move on
        elif (white_or_yellow is True):  # If white or yellow is true then the letter exists in the secret, just not the right place 
            output = output + yellow_box  # Add a yellow box and move on
        elif (white_or_yellow is False):  # If white or yellow is false then the letter does not exist in the secret word
            output = output + white_box  # Add a white box and move on
        ind = ind + 1  # counter add and repeat
    return output  # Return the total output


def input_guess(ex_length: int) -> str:  # function to get a proper input
    """Tests to make sure the guess is the right length and returns a valid awnser."""
    output: str = input(f"Enter a {ex_length} character word: ")  # Asking for input first time
    while (ex_length != len(output)):  # repeat while the guess length is not equal to the secret word length
        output = input(f"That wasn't {ex_length} chars! Try again: ")  # prompting for new input 
    return output  # return proper string length 


def main() -> None:  # Main game 
    """The entry to the loop of the game."""
    ind: int = 1  # 46-49 are declarations for counter, secret word, user guess, and the return boxes
    secret_word: str = "codes"
    user_guess: str = ""
    codified_awnser: str = ""

    while (ind < 7):  # Loop 6 times
        print(f"=== Turn {ind}/6 ===")  # formatting
        user_guess = input_guess(len(secret_word))  # user_guess will be a valid entry (lines 37-42)
        codified_awnser = emojified(user_guess, secret_word)  # The valid entry will be ran thru emojified to get proper output (Emojified lines 16-35) & (Contains_char is used within this funtion lines and can be found at lines 5-14)
        if (user_guess == secret_word):  # If the user guessed the righ word print the codified green boxes, winning output, and exit
            print(codified_awnser)
            print(f"You won in {ind}/6 turns!")
            ind = ind + 7
        else:  # if the user didn't guess the correct word then print out the codified corrisponding boxes, increase counter, and reprompt at line(51)
            ind = ind + 1
            print(codified_awnser)
        if (ind == 7):
            print("X/6 - Sorry, try again tomorrow!")  # Used up all you guesses and are kicked out


if __name__ == "__main__":
    main()