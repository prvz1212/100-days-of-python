print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ \n"))
tip = int(input("What percentage tip would you like to give? 10 or 12 or 15 ? \n"))
people = int(input("How many people to split the bill? \n"))
total_tip_amount = (((tip/100)*bill)+bill)
tip_per_person = round((total_tip_amount/people),2)
print(f"Each one should pay $ {tip_per_person}")
