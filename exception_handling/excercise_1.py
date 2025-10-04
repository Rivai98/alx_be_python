number1= int(input("Enter a First number"))
number2= int(input("Enter a second number"))

try:
    
    result=  number1/number2

except ZeroDivisionError as e:
    print(f"Can not divide by zero {e}") 
else:
    
    print(result)
