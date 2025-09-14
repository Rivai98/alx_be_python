user_income = float(input("Enter your monthly income: "))
user_expense = float(input("Enter your monthly Expenses: "))
monthly_savings = user_income - user_expense
year_savings = monthly_savings *12 + (monthly_savings *12 * 0.05)
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${year_savings}")
