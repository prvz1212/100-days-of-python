import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game = [rock, paper, scissors]
# print(game[0])
user_decision = int(input("Enter 0 for rock, 1 for paper and 2 for scissors: "))
if user_decision >= 3 or user_decision <0:
    print("invalid decision, please choose the correct number")
else:
    print(game[user_decision])
    computer_decision = 2
    print(game[computer_decision])
    if user_decision == computer_decision:
        print("It is draw, refresh and play again")
    elif user_decision == 0 and computer_decision == 2:
        print("You won")
    elif computer_decision ==0 and user_decision == 2:
        print("you lost")
    elif user_decision > computer_decision:
            print("You won")
    elif computer_decision > user_decision:
        print("you lost")
    else:
        print("invalid")
