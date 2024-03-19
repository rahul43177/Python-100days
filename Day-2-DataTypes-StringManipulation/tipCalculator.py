print("Welcome to the tip calculator : ")
bill = float(input("What was the total bill : "))
tip = float(input("How much tip would you like to give ? 10, 12, or 15 ? : "))
people = int(input("How many people to split the bill : "))
tip_percent = bill * tip / 100
total_bill = bill + tip_percent
perPerson = total_bill/people

print(f"Each person should play : ${perPerson}")
