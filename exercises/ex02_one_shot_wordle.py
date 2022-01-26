"""Python implementation of Wordle."""

__author__ = "730324058"

from ast import withitem


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

word: str = "python"

usr_guess: str = input(f"What is your {len(word)}-letter guess? ")

while len(usr_guess) != len(word):
    usr_guess = input(f"That was not {len(word)} letters! Try again: ")

i: int = 0
result: str = ""

while i < len(word):
    if usr_guess[i] == word[i]:
        result += GREEN_BOX
    else:
        character_found: bool = False
        j: int = 0
        while j < len(word):
            if usr_guess[i] == word[j]:
                character_found = True
            j += 1
        if character_found:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    i += 1

print(result)

if usr_guess == word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")