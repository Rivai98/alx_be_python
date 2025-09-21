# Match Case Calculator
# This script performs basic arithmetic operations using match-case statements

# Prompt for user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation using Match Case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    
    case _:
        print("Error: Invalid operation! Please use +, -, *, or /")   