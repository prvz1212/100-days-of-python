import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))



# Easy level
# a=""
# for i in range(0, nr_letters):
#     a += random.choice(letters)
# for i in range(0, nr_symbols):
#     a += random.choice(symbols)
# for i in range(0, nr_numbers):
#     a += random.choice(numbers)
#
# print(a)

#hard level
# password_list=[]
# for i in range(0, nr_letters):
#     password_list.append(random.choice(letters))
# for i in range(0, nr_symbols):
#     password_list.append(random.choice(symbols))
# for i in range(0, nr_numbers):
#     password_list.append(random.choice(numbers))
#
# print(password_list)
# random.shuffle(password_list)
#
# password = ""
# for i in password_list:
#     password += i
#
# print(f"Your password is {password}")


#randomly create the password
password = letters
password.extend(symbols)
password.extend(numbers)
random.shuffle(password)
password_length = random.randint(12, 18)
password_list =[]
for i in range(0, password_length):
    password_list.append(random.choice(password))

new_password = ""
for x in password_list:
    new_password +=x

print(f"Your new password is {new_password}")