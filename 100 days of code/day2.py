print("Welcome to the tip calculator!")
total_bill=input("What was the total bill? ")
tip=input("How much tip would you like to give? 10, 12, or 15? ")
people=input("How many people to split the bill? ")
final_total_bill=float(total_bill)
final_tip=int(tip)
total_people=int(people)
x=final_tip/100*final_total_bill
y=x+final_total_bill
z=round(y/total_people,2)
z="{:.2f}".format(z)
print(f"Each person should pay: ${z}")