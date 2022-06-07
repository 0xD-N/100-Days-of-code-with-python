coffee_machine = {
    "water": [300, "ml"],
    "milk": [200, "ml"],
    "coffee": [100, "g"],
    "cash": 0
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

change = {
    "quarter" : 0.25,
    "dime" : 0.10,
    "nickel": 0.05,
    "penny": 0.01
}
# 1: print report of coffee machine
def printReport():
    
    print(f"\nwater: {coffee_machine['water'][0]}{coffee_machine['water'][1]}")
    print(f"\nmilk: {coffee_machine['milk'][0]}{coffee_machine['milk'][1]}")
    print(f"\ncoffee: {coffee_machine['coffee'][0]}{coffee_machine['coffee'][1]}")
    print(f"\ncash: ${coffee_machine['cash']}")

# checks if there are enough resources to make the provided optiono
def sufficient_resources(option):
    
    sufficient = True
    
    insufficient_resouces = []
    # loop through ingredients dictionary for a specific option in the menu
    for ingredient, quantity in MENU[option]["ingredients"].items():
        
        # if any ingredient in the coffe machine is less than the required amount(quantity) to make the option, set sufficient to false
        
        if coffee_machine[ingredient][0] < quantity:
            sufficient = False
            insufficient_resouces.append(ingredient)

    if sufficient == False:
        print(f"\nInsufficient resources to make {option}. Missing resoures: {', '.join(insufficient_resouces)}")
    return sufficient

def transaction_success(option, quarters, dimes, nickels, pennies):
    
    total = (change["quarter"] * quarters) + (change["dime"] * dimes) + (change["nickel"] * nickels) + (change["penny"] * pennies)
    
    if total > MENU[option]["cost"]:
        print(f"\nHere's ${round(total - MENU[option]['cost'], 2)} dollars in change.")
        return True
    elif total == MENU[option]["cost"]:
        return True
    else:
        return False
    

def deduct_ingredients(option):
    
    for ingredient, quantity in MENU[option]["ingredients"].items():
        
        coffee_machine[ingredient][0] -= quantity
        

user_input = ""

# 2: turn off coffee machine by inputting off
while user_input != "off":
    
    user_input = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    
    # 3: WHen user enter's "report", a report should be generateed that shows current resource values
    if user_input == "report":
        printReport()
    elif user_input == "refill":
        coffee_machine["water"][0] = 300
        coffee_machine["milk"][0] = 200
        coffee_machine["coffee"][0] = 100
        
        print("\nCoffee machine restocked!")
    elif user_input in MENU:
        
        # 4: Check if resources are sufficient 
        if sufficient_resources(user_input):
            
            # 5: Process coins
            print("\nPlease insert coins")
            
            quarters = int(input("\nHow many quarters?: "))
            
            dimes = int(input("\nHow many dimes?: "))
            
            nickels = int(input("\nHow many nickels?: "))
            
            pennies = int(input("\nHow many pennies?: "))
            
            # 6: Check if transaction successful
            if transaction_success(user_input, quarters,dimes,nickels,pennies):
                coffee_machine["cash"] += MENU[user_input]["cost"]
                
                deduct_ingredients(user_input)
                
                print(f"\nHere's your {user_input}. Enjoy!")
            else:
                print("\nSorry that's not enough money. Money refunded.")
                