# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


#pow() is a built in function that raises a number to a power

#float() converts strings into floating point numbers
bmi = weight / pow(height, 2)

category = "";

if(bmi < 18.5):
    print(f"Your BMI is {int(round(bmi, 0))}, you are underweight.")
elif(bmi >= 18.5 and bmi < 25):
    print(f"Your BMI is {int(round(bmi, 0))}, you have a normal weight.")
elif(bmi >= 25 and bmi < 30):
    print(f"Your BMI is {int(round(bmi, 0))}, you are slightly overweight.")
elif(bmi >= 30 and bmi < 35):
    print(f"Your BMI is {int(round(bmi, 0))}, you are obese.")
elif(bmi > 35):
    print(f"Your BMI is {int(round(bmi, 0))}, you are clinically obese.")
    
# Note: Be careful of the sample input, as it has height and weight swapped from code produced from editor. 

