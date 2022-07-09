print("Hey I am leap year indentifer!")
print("How may I Help you!")
year=int(input("Please enter the year which you would like to find leap year or not:"))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("It is leap year")
    else:
      print("Sorry it is not a leap year")
  else:
    print("It is a leap year")  
else:
  print("Sorry it is not a leap year")
