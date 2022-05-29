#ascii art from https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

import random

from urandom import choice

computerChoice = random.randint(0,2)
computerHand = ""

if computerChoice == 0:
    
    computerHand ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
elif computerChoice == 1:
    
    computerHand = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

elif computerChoice == 2:
    
    computerHand = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#end of computer

#start of user
userChoice = int(input("\nWhat do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
userHand = ""

if userChoice == 0:
    
    userHand ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
elif userChoice == 1:
    
    userHand = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

elif userChoice == 2:
    
    userHand = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print(f"\n{userHand}\n\nComputer chose: \n{computerHand}")

#determins tie and win scenarios. If no scenario is met, it is a loss
if userChoice == computerChoice:
    print("Tie!")
elif userChoice == 0 and computerChoice == 2:
    print("You win!")
elif userChoice == 1 and computerChoice == 0:
    print("You win!")
elif userChoice == 2 and computerChoice == 1:
    print("You win!")
else:
    print("You lose.")
    
