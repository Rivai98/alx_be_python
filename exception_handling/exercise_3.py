class ValueTooHighError(Exception): 

    def __init__(self, number):
        self.number = number

    def __str__(self):
        
        return f"the {self.number} value is greater than 100"
           
            
    
try:
    number= int(input("Enter a number :"))
    if number > 100:
        raise ValueTooHighError(number)
    
except ValueError:
    print("Invalid input! Please enter a valid number.")

except ValueTooHighError as e:
    print(e)

else:
    print(f"The number {number} is valid")





