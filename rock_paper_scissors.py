import random

choices = ('r', 'p', 's')
choice_meaning  = {'r': 'Rock', 's': 'Scissors', 'p': 'Paper'}

while True:
    user_choice = input("Rock, Paper or Scissors? (r/p/s): ")
    if user_choice not in choices:
        print('Invalid Choice')
        continue
        
    computer_choice = random.choice(choices)
    print(f'You Chose {choice_meaning[user_choice]}')
    print(f'Computer Chose {choice_meaning[computer_choice]}')
    
    if (user_choice == computer_choice):
        print("It's a Tie!!!")
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print("You Win!!!")
    else:
        print("You Lose!!!")
        
    should_continue = input("Do You Want To Continue? (y/n): ")
    if should_continue == 'n':
        print("Thanks for Playing the Game, Goodbye!!!")
        break