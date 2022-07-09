print("Hey I am BMI calculator")
weight=int(input("Enter your weight in kg: "))
height=float(input("Enter your height in m: "))
bmi=round(weight/(height**2))
if bmi<18.5:
  print(f"Your BMI value is {bmi} , you are underweight")
elif bmi<25:
    print(f"Your BMI value is {bmi} , you are normalweight")
elif  bmi<30:
  print(f"Your BMI value is {bmi} , you are overweight")
elif bmi<35:
  print(f"Your BMI value is {bmi} , you are obese")
elif bmi>35:
  print(f"Your BMI value is {bmi} , you are Clinically obese")