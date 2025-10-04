def safe_divide(numerator, denominator):

    try:
        num = float(numerator)
        den = float(denominator)
        result= num / den
        print(f"The result of the division is {result:.1f}")
        
            
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
    except ValueError as e :
        print("Error: Please enter numeric values only.")
 

        

