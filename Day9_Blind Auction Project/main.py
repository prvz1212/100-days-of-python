# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art
import find_highest as fh

print(art.logo)

want_to_bit = False
bidders = {}
while not want_to_bit:
    name = input("Enter your name: ")
    price = int(input("Enter your bid Amount $ "))
    bidders[name] = price
    again = input("Is there anyone else to bid ?: Type 'y' or 'n' : ").lower()
    if again == 'y':
        print("\n" *20)
    elif again =='n':
        want_to_bit = True
        fh.find_highest_bid(bidders)
    else:
        print("Invalid input, try again")






