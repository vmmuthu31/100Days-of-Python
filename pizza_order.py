print("Welcome to Python Pizza Deliveries!!!")
size=input("Enter the size of the pizza which you like to buy:\n1.small\n2.medium\n3.large\nEnter the your wish:")
if size == "small":
  bill=199
  print("Thank you for ordering Small size pizza\nYour bill amount is Rs.199")
elif size == "medium":
  bill=299
  print("Thank you for ordering Medium size pizza\nYour bill amount is Rs.299")
elif size == "large":
  bill=499
  print("Thank you for ordering Large size pizza\nYour bill amount is Rs.499")
add_pepperonion=input("Do you want pepperonion? Yes or No: ")
if add_pepperonion == "Yes":
  bill += 50
  print(f"The cost of pepperion is Rs.50. Now your Total bill is Rs.{bill}")
else:
  print("Your welcome!")
extra_cheese=input("Do you want extra cheese? Yes or No: ")
if extra_cheese == "Yes":
  bill+=25
  print(f"The cost of extra cheese is Rs.25. Now your Total bill is Rs.{bill}\nHave a great Day!!!")
else:print(f"Now your Total bill is Rs.{bill}.\nHave a great Day!!!")