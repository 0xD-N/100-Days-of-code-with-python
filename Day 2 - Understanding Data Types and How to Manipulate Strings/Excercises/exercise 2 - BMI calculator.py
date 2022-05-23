# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#pow() is a built in function that raises a number to a power

#float() converts strings into floating point numbers
bmi = float(weight) / pow(float(height), 2)

#int() truncates the float leaving out the decimal point
print(int(bmi))

# Note: Be careful of the sample input, as it has height and weight swapped from code produced from editor. 