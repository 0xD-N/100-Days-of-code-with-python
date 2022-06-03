student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

def getGrade(num):
    
    if(num >= 91):
        return "Outstanding"
    elif num >= 81:
        return "Exceeds Expectations"
    elif num >= 71:
        return "Acceptable"
    elif num <= 70:
        return "Fail"

for key, value in student_scores.items():
    
    student_grades.update({key: getGrade(value)})

# 🚨 Don't change the code below 👇
print(student_grades)