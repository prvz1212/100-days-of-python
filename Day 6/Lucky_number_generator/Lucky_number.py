def get_user_name():
    name = input(" What's your name? ")
    print(f"Hello {name}")

import random
print("Welcome to the lucky number generator")
get_user_name()
lucky_number = random.randint(0, 10)
print(f"your lucky number today is {lucky_number}")