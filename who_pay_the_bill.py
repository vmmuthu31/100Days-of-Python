import random
name=input("Give me everybody name, seperated by a comma. ")
name_split=name.split(",")
pay=random.choice(name_split)
print(f"{pay} is going to pay the bill")
