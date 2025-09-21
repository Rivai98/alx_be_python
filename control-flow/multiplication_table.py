# Multiplication Table Generator using Match-Case
# This script asks the user for a number and prints its multiplication table from 1 to 10

# Prompt user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table using match-case
print(f"\nMultiplication table for {number}:")
print("-" * 30)

for i in range(1, 11):
    match i:
        case 1:
            product = number * i
            print(f"{number} * {i} = {product}")
        case 2:
            product = number * i
            print(f"{number} * {i} = {product}")
        case 3:
            product = number * i
            print(f"{number} * {i} = {product}")
        case 4:
            product = number * i
            print(f"{number} * {i} = {product}")
        case 5:
            product = number * i
            print(f"{number} * {i} = {product}")
        case 6:
            product = number * i
            print(f"{number} * {i} = {product}")
        case 7:
            product = number * i
            print(f"{number} * {i} = {product}")
        case 8:
            product = number * i
            print(f"{number} * {i} = {product}")
        case 9:
            product = number * i
            print(f"{number} * {i} = {product}")
        case 10:
            product = number * i
            print(f"{number} * {i} = {product}")
        case _:
            print(f"Unexpected multiplier: {i}")