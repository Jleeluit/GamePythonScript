import random

def play_game():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "kiwi", "lemon", "mango", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
    secret_word = random.choice(words).lower()
    guessed_letters = set()
    attempts = 6

    print("Welcome to the Word Guessing Game!")
    print("I have chosen a secret word. Try to guess the word by guessing one letter at a time.")
    print(f"You have {attempts} attempts to guess the word.")

    while attempts > 0:
        print(" ".join([letter if letter in guessed_letters else "_" for letter in secret_word]))
        guess = input("Enter your guess (a-z): ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter (a-z).")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct!")
        else:
            print("Incorrect.")
            attempts -= 1

        if "_" not in [letter if letter in guessed_letters else "_" for letter in secret_word]:
            print(f"Congratulations! You guessed the word '{secret_word}'!")
            break

        print(f"You have {attempts} attempts remaining.")

    if attempts == 0:
        print(f"You have used up all your attempts. The correct word was '{secret_word}'.")

play_game()
