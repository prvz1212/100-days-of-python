from art import logo, vs
from game_data import data
from random import choice


def get_data(a):
    name = a["name"]
    desc = a["description"]
    country = a["country"]
    return f"{name}, a {desc}, from {country}"


def check(guess, a, b):
    if guess == 'a':
        if a > b:
            return True
        else:
            return False
    else:
        if b > a:
            return True
        else:
            return False


print(logo)
points = 0
to_play = True
data2 = choice(data)
while to_play:
    data1 = data2
    data2 = choice(data)
    if data1 == data2:
        data2 = choice(data)
    print(f"Compare A: {get_data(data1)}")
    print(vs)
    print(f"Compare B: {get_data(data2)}")
    followers1 = data1["follower_count"]
    followers2 = data2["follower_count"]
    print(f"{followers1} and {followers2}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if check(guess, followers1, followers2):
        points += 1
        print(f"You're right! Current score is {points}")
    else:
        print(f"Sorry ! You are wrong. Final score is {points}")
        to_play = False
