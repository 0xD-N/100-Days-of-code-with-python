# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#add numbers using for loop

# divide sum by length, round number accordingly to the nearest whole number, and then cast into an integer to lose decimal precision for correct output\

total = 0

for num in student_heights:
    total += num

print(int(round(total / len(student_heights), 0)))