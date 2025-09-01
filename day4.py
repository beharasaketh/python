import random
rock = '''
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock,paper,scissors]
computer_choice = random.randint(0,2)
user_choice = int(input("what do you choose? type 0 for rock , 1 for paper, 2 for scissors "))
print(game[user_choice])
print(f"computer choose:"
      f"{game[computer_choice]}")
if 3 <= user_choice < 0:
      print("invalid number try again")
elif user_choice == 0 and computer_choice == 2:
      print("you won")
elif user_choice == 2 and computer_choice == 0:
      print("you lose")
elif computer_choice > user_choice:
      print("you lose")
elif user_choice > computer_choice:
      print("won")
elif user_choice == computer_choice:
      print("draw")








