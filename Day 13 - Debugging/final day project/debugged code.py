############DEBUGGING#####################


# # Describe Problem

#the function never reaches 20 due to 20 being exclusive in the for loop
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()

# # Reproduce the Bug

# the bug is that random int starts at 1 and ends a 6, with 6 also included. 6 is out of bounds, and index 0 is never included.

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# #dice_num = randint(1, 6)
# dice_num = randint(0, len(dice_imgs) - 1)
# print(dice_imgs[dice_num])



# # Play Computer

# Bugs:
# - 1994 is not included
# - years before 1980 along with 1980 itself is not included

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")


# Bug: age was not casted into an integer. Format specifier was also not included for string

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
# print(f"You can drive at age {age}.")

# Bug: comparison operator in use in place of assignment operator

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# Bug: new_item only exists within scope of for loop. Indentation for line 64 fixes issue. Now statement exists in same scope as new_item

# #Use a Debugger
# def mutate(a_list):
#   b_list = []

#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])