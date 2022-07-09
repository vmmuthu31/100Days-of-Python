print("Hello.... \nI am a love calculator!!!")
name1=input("Enter Your Name: ")
name2=input("Enter Your Lover Name: ")
combined_name=name1+name2
name=combined_name.lower()
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
true=t+r+u+e
l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
love=l+o+v+e
love_score=int(str(true)+str(love))
if (love_score < 10) or (love_score > 90):
  print(f"Your love score is {love_score}. You are couple are like Hydrogen and Oxygen in water")
elif (love_score >= 40) and (love_score <= 50):
  print(f"Your love score is {love_score}. You are alright together")
else:
  print(f"Your score is {love_score}")