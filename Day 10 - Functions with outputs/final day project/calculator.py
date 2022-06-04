from art import logo


def add(num, num2) -> float:
    return num + num2

def subtract(num, num2) -> float:
    return num - num2

def multiply(num, num2) -> float:
    return num * num2

def divide(num, num2) -> float:
    return num / num2

operations = {
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(logo)

choice = ""

num1 = 0
num2 = 0
result = 0

while choice != "exit":
    
    
    if choice != "y":
        
        num1 = float(input("\nWhat is the first number?: "))
        num2 = 0
    else:
        num1 = result
    
    print("\n[ + , - , * , / ]")
    
    op = input("\nPick an operation: ")
    
    if op in operations:
        
        num2 = float(input("\nWhat is the second number?: "))
        
        result = operations[op](num1, num2)
        print(f"\n{num1} {op} {num2} = {result}")
        
    
    choice = input(f"\nEnter 'y' to keep calculating with {result}. Enter 'n' to start a new calculation. Enter 'exit' to quit: ").lower()
    
