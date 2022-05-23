print("Welcome to the tip calculator.")

# taking user input and casting into proper numbers
billTotal = float(input("\nWhat was the total bill? $"))

tipPercentage = int(input("\nWhat percentage tip would you like to give? "))

splitAmount = int(input("\nHow many people are you splitting with? "))

#calculating tip
tip = (float(tipPercentage)/100) * billTotal

#calculating cost per person with tip included
totalWithTip = billTotal + tip

costPerPerson = totalWithTip / splitAmount

#outputting result

#round is a built in function that rounds a number to a given precision

print(f"\nEach person should pay ${round(costPerPerson, 2)}")