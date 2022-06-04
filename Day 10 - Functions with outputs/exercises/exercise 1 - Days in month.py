def is_leap(year):
  
  return True if (year % 4 == 0 and year % 100 != 0) or year % 4 == 0 and year % 400 == 0 else False

def days_in_month(year, month):
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    
    if is_leap(year):
        month_days[1] = 29
        
    return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
