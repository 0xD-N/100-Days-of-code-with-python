from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
CashMachine = MoneyMachine()

user_input = ""

while user_input != "off":
    
    user_input = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    
    if user_input == "off":
        break
    elif user_input == "report":
        machine.report()
        print(f"cash: ${CashMachine.profit}")
    else:
        selection = menu.find_drink(user_input)
        
        if(selection):
            
            if machine.is_resource_sufficient(selection):            
                
                if(CashMachine.make_payment(selection.cost)):
                    machine.make_coffee(selection)
                
                
            