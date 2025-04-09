import helper as hp
to_play = True
while to_play:
    hp.greet()
    hp.guessing_game()
    user_input2 = input("Do you want to play again? 'y' or 'n' ").lower()
    if user_input2 == 'y':
        print("\n" * 10)
    else:
        print("Thanks for your time ")
        to_play = False

