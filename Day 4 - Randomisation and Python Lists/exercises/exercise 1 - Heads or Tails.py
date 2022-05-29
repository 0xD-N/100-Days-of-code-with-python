#Remember to use the random module
import random
import time
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇

# 1 - heads
# 0 - tails

randNumber = random.randint(0,1)

print("Heads" if randNumber == 1 else "Tails")