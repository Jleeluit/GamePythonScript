import random

# set up the game loop
play_again = 'y'
while play_again == 'y':
    # get user's preferred difficulty level
    difficulty = input('Choose a difficulty level (easy, medium, hard): ')
    
    # set up the number range based on difficulty level
    if difficulty == 'easy':
        min_num = 1
        max_num = 10
    elif difficulty == 'medium':
        min_num = 10
        max_num = 50
    elif difficulty == 'hard':
        min_num = 50
        max_num = 100
    
    # generate a random math problem
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    operator = random.choice(['+', '-', '*', '/'])
    
    # ask the user to solve the problem
    user_answer = input(f'What is {num1} {operator} {num2}? ')
    
    # check if the user's answer is correct
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    elif operator == '/':
        correct_answer = num1 / num2
    
    if float(user_answer) == correct_answer:
        print('Correct!')
    else:
        print(f'Incorrect. The correct answer is {correct_answer}.')
    
    # ask the user if they want to play again
    play_again = input('Do you want to play again? (y/n) ')
