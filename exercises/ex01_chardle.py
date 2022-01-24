"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730324058"

usr_input: str = input("Enter a 5-character word: ")
if len(usr_input) != 5:
    print("Error: word must contain 5 characters")

usr_input_char: str = input("Enter a single character: ")
if len(usr_input_char) != 5:
    print("Error: Character must be a single character.")

print("Searching for " + usr_input_char + " in " + usr_input)
occurrence_sum: int = 0


if usr_input[0] == usr_input_char:
    print(usr_input_char + " found at index 0")
    occurrence_sum += 1

if usr_input[1] == usr_input_char:
    print(usr_input_char + " found at index 1")
    occurrence_sum += 1

if usr_input[2] == usr_input_char:
    print(usr_input_char + " found at index 2")
    occurrence_sum += 1

if usr_input[3] == usr_input_char:
    print(usr_input_char + " found at index 3")
    occurrence_sum += 1

if usr_input[4] == usr_input_char:
    print(usr_input_char + " found at index 4")
    occurrence_sum += 1

if occurrence_sum > 0:
    print(str(occurrence_sum) + " instances of " + usr_input_char + " found in " + usr_input)
else:
    print("No instances of " + usr_input_char + " found in " + usr_input)