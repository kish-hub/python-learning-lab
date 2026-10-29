"""Practice while loops, comparisons, and input validation with a guessing game."""

import random

MIN_NUMBER = 1
MAX_NUMBER = 20
MAX_ATTEMPTS = 5


def check_guess(guess: int, secret: int) -> str:
    """Give a hint about how a guess compares with the secret number."""
    if guess < secret:
        return "Too low."
    if guess > secret:
        return "Too high."
    return "Correct!"


def get_valid_guess() -> int:
    """Keep asking until the player enters a whole number in range."""
    while True:
        answer = input(f"Enter a number ({MIN_NUMBER}-{MAX_NUMBER}): ")
        try:
            guess = int(answer)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print(f"Choose a number from {MIN_NUMBER} to {MAX_NUMBER}.")
            continue
        return guess


def play_game() -> None:
    """Let the player guess a random number within a fixed attempt limit."""
    secret = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0
    print(f"Guess the number from {MIN_NUMBER} to {MAX_NUMBER}!")
    print(f"You have {MAX_ATTEMPTS} attempts.")

    while attempts < MAX_ATTEMPTS:
        try:
            guess = get_valid_guess()
        except (EOFError, KeyboardInterrupt):
            print("\nGame cancelled.")
            return

        attempts += 1
        print(check_guess(guess, secret))
        if guess == secret:
            print(f"You found it in {attempts} attempt(s).")
            return

        if attempts < MAX_ATTEMPTS:
            print(f"{MAX_ATTEMPTS - attempts} attempt(s) remaining.")

    print(f"Out of attempts. The number was {secret}.")


if __name__ == "__main__":
    play_game()
