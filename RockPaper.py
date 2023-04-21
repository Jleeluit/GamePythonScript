import random

print("Welcome to Rock, Paper, Scissors!")
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

while True:
    player_choice = input("Enter your choice (rock, paper, or scissors): ")

    if player_choice not in options:
        print("Invalid choice. Try again.")
        continue

    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (y/n) ")
    if play_again != "y":
        break

    computer_choice = random.choice(options)
