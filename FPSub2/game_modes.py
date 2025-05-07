import random
from config import DEFAULT_MEDIUM_ROUNDS, MAX_HARVARD_ROUNDS
from utils import (
    get_random_secret,
    get_clues_for_position,
    update_scoreboard,
)

def play_easy():
    secret = get_random_secret()
    try:
        rounds = int(input("How many rounds would you like? ").strip())
        if rounds < 1:
            raise ValueError
    except ValueError:
        print("Invalid. Defaulting to 5 rounds.")
        rounds = 5

    for r in range(1, rounds + 1):
        clue = random.choice(get_clues_for_position(secret))
        low, high = clue["spectrum"]
        print(f"\nRound {r}/{rounds}")
        print(f"{low} ←———→ {high}")
        print(f"Clue: {clue['word']}")
        try:
            guess = int(input("Your guess (1–10): ").strip())
        except ValueError:
            print("✗ Enter a number 1–10.")
            continue

        if guess == secret:
            print("Correct!")
            update_scoreboard("Easy", True)
            return
        elif guess < secret:
            print("A little higher, almost there.")
        else:
            print("A little lower, try again.")

    print(f"\nOut of rounds! The secret number was {secret}.")
    update_scoreboard("Easy", False)


def play_medium():
    secret = get_random_secret()
    rounds = DEFAULT_MEDIUM_ROUNDS
    print(f"\nMedium mode: {rounds} rounds with hints.")

    for r in range(1, rounds + 1):
        clue = random.choice(get_clues_for_position(secret))
        low, high = clue["spectrum"]
        print(f"\nRound {r}/{rounds}")
        print(f"{low} ←———→ {high}")
        print(f"Clue: {clue['word']}")
        try:
            guess = int(input("Your guess (1–10): ").strip())
        except ValueError:
            print("✗ Enter a number 1–10.")
            continue

        if guess == secret:
            print("Correct!")
            update_scoreboard("Medium", True)
            return
        elif guess < secret:
            print("A little higher, almost there.")
        else:
            print("A little lower, try again.")

    print(f"\nOut of rounds! The secret number was {secret}.")
    update_scoreboard("Medium", False)


def play_harvard():
    secret = get_random_secret()
    rounds = MAX_HARVARD_ROUNDS
    print(f"\nHarvard mode: {rounds} rounds, no hints.")

    for r in range(1, rounds + 1):
        clue = random.choice(get_clues_for_position(secret))
        low, high = clue["spectrum"]
        print(f"\nRound {r}/{rounds}")
        print(f"{low} ←———→ {high}")
        print(f"Clue: {clue['word']}")
        try:
            guess = int(input("Your guess (1–10): ").strip())
        except ValueError:
            print("✗ Invalid input.")
            continue

        if guess == secret:
            print("Correct!")
            update_scoreboard("Harvard", True)
            return
        else:
            print("✗ Wrong.")

    print(f"\nAll done! The secret number was {secret}.")
    update_scoreboard("Harvard", False)