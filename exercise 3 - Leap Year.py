# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


print("Leap year." if (year % 4 == 0 and year % 100 != 0) or year % 4 == 0 and year % 400 == 0 else "Not leap year.")