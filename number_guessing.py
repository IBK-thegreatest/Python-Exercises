import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input("Enter a Number between 1 and 100: "))
        if guess > number_to_guess:
            print("Too High!")
        elif guess < number_to_guess:
            print("Too Low!")
        else:
            print("Congratulations, You Guessed the Correct Number")
            break
    except ValueError:
        print("Please Enter a Valid Number")