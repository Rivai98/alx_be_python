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
            product = number * 1
            print(f"{number} * 1 = {product}")
        case 2:
            product = number * 2
            print(f"{number} * 2 = {product}")
        case 3:
            product = number * 3
            print(f"{number} * 3 = {product}")
        case 4:
            product = number * 4
            print(f"{number} * 4 = {product}")
        case 5:
            product = number * 5
            print(f"{number} * 5 = {product}")
        case 6:
            product = number * 6
            print(f"{number} * 6 = {product}")
        case 7:
            product = number * 7
            print(f"{number} * 7 = {product}")
        case 8:
            product = number * 8
            print(f"{number} * 8 = {product}")
        case 9:
            product = number * 9
            print(f"{number} * 9 = {product}")
        case 10:
            product = number * 10
            print(f"{number} * 10 = {product}")
        case _:
            print(f"Unexpected multiplier: {i}")