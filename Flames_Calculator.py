print("Hello Buddy!!!... ")
print("Welcome to flames calculator")
name1=input("Enter your name: ")
name2=input("Enter your lover name: ")
combined_name=name1+name2
name=combined_name.lower()
f=name.count("f")
l=name.count("l")
a=name.count("a")
m=name.count("m")
e=name.count("e")
s=name.count("s")
highest_value=[f,l,a,m,e,s]
if f== max(highest_value):
  print("Your his/her friend!")
elif l== max(highest_value):
  print("Your his/her lover!")
elif a== max(highest_value):
  print("Your his/her affectioner")
elif m== max(highest_value):
  print("Your his/her future girl/boy!")
elif e== max(highest_value):
  print("Your his/her enemy!")
elif s== max(highest_value):
  print("Your his/her sister!")

