from art import logo
import random
import os

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_hand = {"cards": [], "total": 0}
user_hand = {"cards": [], "total": 0}


choice = input("\nDo you want to play a game of blackjack? Type 'y' or 'n': ").lower()

if choice == "y":
    
    os.system("cls")
    print(f"\n{logo}")
    
    user_hand["cards"].append(deck[random.randint(0, len(deck) - 1)])
    user_hand["cards"].append(deck[random.randint(0, len(deck) - 1)])
    
    user_hand["total"] = sum(user_hand["cards"])
    
    computer_hand["cards"].append(random.randint(0, len(deck) - 1))
    computer_hand["cards"].append(random.randint(0, len(deck) - 1))
    
    computer_hand["total"] = sum(computer_hand["cards"])
    
    print(f"\nYour cards: {user_hand['cards']}")
    
    print(f"\nComputer's first card: {computer_hand['cards'][0]}")
    
    choice = input("\nType 'y' to hit or type 'n' to stand: ")
    
    if choice == 'y':
        
        while choice == "y" and user_hand["total"] < 21:
            
            user_hand["cards"].append(deck[random.randint(0, len(deck) - 1)])
            
            user_hand["total"] = sum(user_hand["cards"])
            
            if user_hand["total"] > 21:
                break
            
            print(f"\nYour current hand: {user_hand['cards']}")
            
            choice = input("\nType 'y' to hit or type 'n' to stand: ")
    
    
    shouldHit = random.randint(0,1)
    
    if shouldHit == 1 and user_hand["total"] < 21:
        
        computer_hand["cards"].append(deck[random.randint(0, len(deck) - 1)])
        
        computer_hand["total"] = sum(computer_hand["cards"])
        
    
    print(f"\nYour final hand: {user_hand['cards']}")
    
    print(f"\nComputer's final hand: {computer_hand['cards']}")
    
    if computer_hand["total"] > 21 and user_hand["total"] > 21:
        print("\nYou both lose!")
    elif computer_hand["total"] == 21:
        print("\nThe computer has got blackjack!")
    elif user_hand["total"] == 21:
        print("\nYou got a blackjack!")
    elif user_hand["total"] > computer_hand["total"]:
        print("\nYou win")
    else:
        print("\nYou lose!")
        
        
        
        
else:
    
    print("\nGoodbye.")

