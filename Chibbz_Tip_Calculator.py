print("Welcome to the Chibbz Tip Calculator!")
bill = float(input("How much is the total bill? $"))
tip = float(input("How much tip would you like to give? 5, 10, 15, or 20? "))
people = int(input("How many people would split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


print(f"Each person should pay: ${final_amount}")
