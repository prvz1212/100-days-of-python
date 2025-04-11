
easy = 10
hard =5

from random import randint
def greet():
    print(r"""  
    ________                                __  .__                                 ___.                 
     /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________ 
    /   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
    \    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
     \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
     """)

    print ("Welcome to the Number Guessing Game!")
    print ("I am thinking of a number between 1 and 100")

def run_out(a,b):
    if a == 0:
        print("You've ran out of guesses")
        print("You lose")
        print (f"The number is {b}")
    else:
        print("Guess again")

def set_difficulty():
    user_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if user_input == 'easy':
        return easy
    elif user_input == 'hard':
        return hard

def guessing_game():
    level = int(set_difficulty())
    com_guess = randint(1, 100)
    # print(com_guess)
    while level > 0:
        print(f"You have {level} attempts remaining to guess the number")
        guess = int(input("Make a guess : "))
        if guess == com_guess:
            print(f"You got it ! The answer was {com_guess}.")
            level = 0
        elif guess > com_guess:
            if guess - com_guess <= 5:
                print("Too close but high")
            elif guess-com_guess <= 15:
                print("Close but high")
            else:
                print("Too high")
            level -= 1
            run_out(level, com_guess)
        elif guess < com_guess:
            if com_guess - guess <= 5:
                print("Too close but low")
            elif com_guess-guess <= 15:
                print("Close but low")
            else:
                print("Too Low")
            level -= 1
            run_out(level, com_guess)
        else:
            print("enter Valid input")
            print("Guess again")
            level -= 1