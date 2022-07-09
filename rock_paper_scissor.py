import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
users_choice=input("What do you choose? Type 0 for Rock,1 for Paper,2 for Scissors.")
computers_choice=random.randint(0,2)
print (f"Computers choice is {computers_choice}")
if users_choice == 0:
  print("It's Rock")
if users_choice == 1:
  print("It's Paper")
if users_choice == 2:
  print("It's Scissors")

if computers_choice == 0:
  print("It's Rock")
if computers_choice == 1:
  print("It's Paper")
if computers_choice == 2:
  print("It's Scissors")
# switcher{
#   case 0:
#     if users_choice==0 and computers_choice==1:
#       print("You win")
#     if users_choice==0 and computers_choice==2:
#       print("You Lose")
#     break;
  
#   case 1:
#     if users_choice==1 and computers_choice==2:
#       print("You Lose")
#     if users_choice==1 and computers_choice==0:
#       print("You Win")
#     break;
#   case 2:
  
#     if users_choice==2 and computers_choice==0:
#       print("You Lose")
#     if users_choice==2 and computers_choice==1:
#       print("You Win")
#     break;
#   default:
#     if users_choice == computers_choice:
#       print("It's Draw")
# }


# game_images = [rock, paper, scissors]