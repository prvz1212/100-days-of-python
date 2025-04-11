import art

print(art.logo)


def add(n1, n2):
    return n1 + n2

def subs(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2



def calculator(n1, symbol):
    to_continue = True
    while to_continue:
        for i in symbol:
            print(i)
        method = input("Enter your operation: ")
        if method not in symbol:
            print("Invalid input, retry again ")
            to_continue = False
        else:
            n2 = float(input("Enter the second number: "))
            answer = round(symbol[method](n1, n2), 2)
            print(answer)
            again = input(f"Do you want to continue with {answer}, Type 'y' or 'n': ").lower()
            if again == 'y':
                n1 = answer
            elif again == 'n':
                to_continue = False
                print("\n" * 10)
            else:
                print("Invalid Input")
                to_continue = False
                print("\n" * 10)


operations = {
    "+": add,
    "-": subs,
    "*":mul,
    "/":div
}


to_be_continued = True

while to_be_continued:
    n1=float(input("Enter the first number: "))
    calculator(n1, operations)

