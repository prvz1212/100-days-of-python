print(r'''
*******************************************************************************
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("where do you want to go? 'left' or 'right': ")
if direction == "left":
    print("You made it through the first challenge")
    print("Oh no! There is a big lake")
    decision = input("Should i wait for the boat or swim ? enter 'wait' or 'swim': ")
    if decision == 'wait':
        print("Hooray! We came across the river")
        print("There are three doors infront of me")
        door = input("Which door should i choose? 'red', 'yellow' or 'blue': ")
        if door == 'yellow':
            print("You found the treasure!!")
            print(r'''
                                        _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
            
            ''')
            print("You win")
        elif door == 'red':
            print("Burned by fire, GAME OVER")
        elif door == 'blue':
            print ("Eaten by beasts, GAME OVER")
        else:
            print ("Wrong decision, GAME OVER")

    elif decision == 'swim':
        print("Attacked by Trout, GAME OVER")
    else:
        print("Wrong decision, GAME OVER")
elif direction == "right":
    print("Fall into a pithole, GAMEOVER")
else:
    print("Wrong decision, GAME OVER")