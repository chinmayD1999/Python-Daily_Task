print("Welcome to the Tip Calculator")
Total_bill = int(input("What was the total bill? \n"))
Tip = int(input("How much tip would you like to give? 10, 12, 15?\n"))
people = int(input("How many people to split the bill? \n"))

tip_amount_in_percentage = Tip / 100
tip_amount_of_bill = tip_amount_in_percentage * Total_bill
Total_bill = Total_bill + tip_amount_of_bill
each_person_bill = Total_bill / people

print("Each person should pay: ", each_person_bill)
