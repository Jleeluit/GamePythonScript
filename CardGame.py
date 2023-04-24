import random

# Define the deck of cards
suits = ['♠', '♡', '♢', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(rank, suit) for rank in ranks for suit in suits]

# Function to shuffle the deck of cards
def shuffle_deck():
    random.shuffle(deck)

# Function to draw a card from the deck
def draw_card():
    return deck.pop(0)

# Function to compare the ranks of two cards
def compare_cards(card1, card2):
    rank1, _ = card1
    rank2, _ = card2
    if ranks.index(rank1) > ranks.index(rank2):
        return 1
    elif ranks.index(rank1) < ranks.index(rank2):
        return -1
    else:
        return 0

# Shuffle the deck
shuffle_deck()

# Draw a card for player 1
player1_card = draw_card()
print("Player 1's card:", player1_card[0])

# Draw a card for player 2
player2_card = draw_card()
print("Player 2's card:", player2_card[0])

# Compare the ranks of the two cards
result = compare_cards(player1_card, player2_card)
if result == 1:
    print("Player 1 wins!")
elif result == -1:
    print("Player 2 wins!")
else:
    print("It's a tie!! Good Game!")

