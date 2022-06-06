from art import logo
import random

# generate random number
secret = random.randint(1,100)

# output instructions to user

# logo
print(logo)

# introduction 
print("\nWelcome to the Number Guessingn Game!\n\nI'm thinking of a number between 1 and 100.")

# get difficulty from user
choice = input("\nChoose a difficulty. Type 'easy' or 'hard': ")

# variable for user's lives and guess
lives = 0
guess = 0

if choice == "easy":
    lives = 10
elif choice == "hard":
    lives = 5
else:
    print("\nInvalid option!")
    
print(f"\nYou have {lives} attempts remaining to guess the number.")
    
while lives > 0 and guess != secret:
    
    guess = int(input("\nGuess a number: "))
    
    if guess < secret:
        lives -= 1
        print(f"\nToo low. You now have {lives} attempts left.")
    elif guess > secret:
        lives -= 1
        print(f"\nToo high. You now have {lives} attempts left.")
        
if guess == secret:
    print(f"\nCongratulations! The number was {secret}!")



