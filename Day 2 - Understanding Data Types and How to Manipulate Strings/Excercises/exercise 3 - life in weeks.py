# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


# age is now a integer and no longer a string
age = int(age)

#90 years to days, weeks, months 
totaldays90 = 90 * 365
totalWeeks90 = 90 * 52
totalMonths90 = 90 * 12

#user's age to days, weeks, months
userAgeToDays = age * 365
userAgeToWeeks = age * 52
userAgeToMonths = age * 12

#output's their time remaining until 90. (Pretty scary)
print(f"You have {totaldays90 - userAgeToDays} days, {totalWeeks90 - userAgeToWeeks} weeks, and {totalMonths90 - userAgeToMonths} months left.")


