import random
from unittest import result

print("\nWelcome to the PyPassword Generator!")

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*()"
numbers = "1234567890"

password = []



letterCount = int(input("\nHow many letters would you like in your password?: "))
symbolCount = int(input("\nHow many symbols would you like in your password?: "))
numberCount = int(input("\nHow many numbers would you like in your password?: "))

totalLength = letterCount + symbolCount + numberCount

l_count = 0
s_count = 0
n_count = 0

for i in range(totalLength):
    password.append("")

while l_count != letterCount:
    
    randIndex = random.randint(0, len(password) - 1)
    
    if len(password[randIndex]) != 0:
        continue
    else:
        password[randIndex] = letters[random.randint(0, len(letters) - 1)]
        l_count += 1
        
while s_count != symbolCount:
    
    randIndex = random.randint(0, len(password) - 1)
    
    if len(password[randIndex]) != 0:
        continue
    else:
        password[randIndex] = symbols[random.randint(0, len(symbols) - 1)]
        s_count += 1
        
while n_count != numberCount:
    
    randIndex = random.randint(0, len(password) - 1)
    
    if len(password[randIndex]) != 0:
        continue
    else:
        password[randIndex] = numbers[random.randint(0, len(numbers) - 1)]
        n_count += 1

newPass = "".join(password)

print(f"\nHere's your password: {newPass}")
        
    
    
    

