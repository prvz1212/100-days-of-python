# from turtle import Turtle, Screen
#
# my_turtle = Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("cyan")
# my_turtle.forward(100)
# print(my_turtle)
#
# my_screen= Screen()
# my_screen.exitonclick()
#
#
#
# from prettytable import PrettyTable
#
# table= PrettyTable()
# table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"])
# table.add_column("Type", ["Elecric", "Water","Fire"])
# table.align = 'l'
# print(table)

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
money = MoneyMachine()
spl = Menu()
is_on = True
while is_on:
    order = input(f"What would you like to drink {spl.get_items()}: ")
    if order == "off":
        is_on = False
    elif order == "report":
        maker.report()
        money.report()
    elif order == "refill":
        maker.refill()
        maker.report()
        money.report()
    else:
        drink = spl.find_drink(order)
        if drink:
            if maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                maker.make_coffee(drink)
