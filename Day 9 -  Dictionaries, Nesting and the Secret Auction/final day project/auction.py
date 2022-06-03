import os
from logo import gavel

bidders = []

name = ""
price = 0
moreBidders = "yes"

print(gavel)

print("Welcome to the secret auction program.")

while moreBidders == "yes":
    
    name = input("\nWhat is your name?: ")
    
    price = int(input("\nWhat's your bid?: $"))
    
    bidders.append({"name": name, "price": price})
    
    print("\nAre there any other biders? Type 'yes' or 'no'.")

    moreBidders = input().lower()
    
    if moreBidders == "yes":
        os.system("cls")
    
bidders.sort(key=lambda x: x["price"])

highest_bidder = bidders.pop()

print(f"\nThe winner is {highest_bidder['name']} with a price of {highest_bidder['price']}")