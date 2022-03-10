"""Python implementation of Wordle."""

__author__ = "730324058"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(search_string: str, search_char: str) -> bool:
    """Searches for search_char in search_word."""
    assert len(search_char) == 1
    i: int = 0
    while i < len(search_string):
        if search_char == search_string[i]:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Match characters and return result emoji string."""
    assert len(guess) == len(secret)
    i: int = 0
    result: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        else:
            character_found: bool = contains_char(secret, guess[i])
            if character_found:
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        i += 1
    return result


def input_guess(secret_length: int) -> str:
    """User input guess."""
    guess: str = input(f"Enter a {secret_length} character word: ")
    while len(guess) != secret_length:
        guess = input(f"That wasn't {secret_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    i: int = 1
    guess: str = ""
    while i <= 6 and guess != secret:
        print(f"=== Turn {i}/6 ===")
        guess = input_guess(len(secret))
        emoji_result: str = emojified(guess, secret)
        print(emoji_result)
        if guess == secret:
            print(f"You won in {i}/6 turns!")
        else:
            i += 1
    if guess != secret:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
