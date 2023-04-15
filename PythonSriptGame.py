#Python Script for Simple Number Guessing Game

import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Number of attempts the player has
attempts = 5

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print(f"You have {attempts} attempts to guess it.")

# Loop for each attempt
for attempt in range(attempts):
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Higher!")
    elif guess > number:
        print("Lower!")
    else:
        print("Congratulations! You guessed it!")
        break

    # Inform the player about remaining attempts
    remaining_attempts = attempts - attempt - 1
    if remaining_attempts > 0:
        print(f"You have {remaining_attempts} attempts left.")
    else:
        print("No attempts left. You lost!")

print(f"The number was: {number}")
print("Thanks for playing!")