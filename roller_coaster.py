print("Hey it is a rollercoaster bill counter!!!")
height=int(input("Enter your height in cm:"))
if height > 125:
  print("Your are eligibe to ride the rollercoaster")
  age=int(input("Enter your age: "))
  if age < 12:
    bill=10
    print("The amount should be paid is Rs.10")
  elif age <= 18:
    bill=25
    print("The amount should be paid is Rs.25")
  elif age >= 18:
    bill=50
    print("The amount should be paid is Rs.50")
  photo=input("Do you want to take photos?? Say Y for Yes and N for No:")
  if photo == "Y":
      bill += 5;
      print(f"The total amount should be paid Rs.{bill}")
  else:
    print(f"That's ok your bill amount will be Rs.{bill}")
else:
  print("Sorry dude! Your are not eligible for riding rollercoaster")