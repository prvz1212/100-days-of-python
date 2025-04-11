from resources import MENU, resources
espresso = MENU["espresso"]
espresso["ingredients"]["milk"] = 0
latte = MENU["latte"]
cap = MENU["cappuccino"]
operating = True
profit = 0

def check(a,b):
    print(f"we have {a["water"]}ml of water" )
    print(f"We have {a["milk"]}ml of milk")
    print(f"We have {a["coffee"]}g of Coffee powder")
    print(f"Total money collected : {b}")

def refill(b):
    b["water"] = 300
    b["milk"] = 300
    b["coffee"] = 100
    return b

def coins(cost):
    print(f"Your coffee is ready to be made and it costs {cost}")
    print("Please insert your coins")
    quarters = int(input("No. of quarters ($0.25): "))
    dimes = int(input("No. of dimes ($0.10): "))
    nickels = int(input("No. of nickels ($0.05): "))
    pennies = int(input("No. of pennies ($0.01): "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    balance = round(total - cost, 2)
    return balance

def admin(source, gain):
    admin_pass = True
    while admin_pass:
        password = input("Printing report, enter your employee password: ")

        if password == 'CoFFee':
            check(source,gain)
            admin_input1 = input("refill needed: 'y' or 'n': ").lower()
            if admin_input1 == 'y':
                refill(source)
                print("Refilled. Now, ")
                check(source, gain)
                print("Exiting admin mode")
                admin_pass = False
            else:
                print("Exiting admin mode")
                admin_pass = False
        else:
            print("Wrong Password, retry with valid password")

def dispense_coffee(list, input,profit):
    choice = list[input]["ingredients"]
    amount = list[input]["cost"]
    if water >= choice["water"] and coffee >= choice["coffee"] and milk >= choice["milk"]:
        change = coins(amount)
        if change >= 0:
            profit = amount
            print("Enjoy your coffee")
            resources["water"] = water - choice["water"]
            resources["milk"] = coffee - choice["coffee"]
            resources["coffee"] = milk - choice["milk"]
            if change > 0:
                print(f"Here is your change ${change}")
        else:
            print("Sorry that's not enough money. Money refunded.")
        return profit
    else:
        print("Not enough materials, please contact admin")






types = [resources, espresso, latte, cap]
#TODO: 1. getting the user request
try:
    while operating:
        user_input = int(input("What would you like to have ? 1 for 'Espresso', 2 for 'latte', 3 for 'Cappuccino' : "))
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        if user_input < 4 and user_input >= 0:
            if user_input == 0:
                admin(resources, profit)
            else:
                profit += dispense_coffee(types, user_input, profit)




except KeyboardInterrupt:
    print("Coffee machine is out of order")
