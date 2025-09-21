# Pattern Drawing Script
# This script uses nested loops to draw a square pattern of asterisks

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
row = 0
while row < size:
    # Use for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    
    # Move to the next line after completing each row
    print()
    
    # Increment row counter
    row += 1