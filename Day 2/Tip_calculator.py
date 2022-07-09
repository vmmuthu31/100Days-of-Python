print("Hey I am the tip Calculator")
bill=float(input("What was the total bill?Rs."))
tip=int(input("What percentage would you live to give? 10,12,15...\n"))
people=int(input("How many people would you like to split?  "))
tip_as_person=tip/100
total_tip_amount=bill*tip_as_person
total_bill= bill+total_tip_amount
bill_per_person=total_bill/people
final_bill=(round(bill_per_person,2))
final_bill="{:.2f}".format(bill_per_person)
print(f"Each person should pay: Rs.{final_bill}"
)