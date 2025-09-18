# Expense Tracker using map

n = int(input("Enter number of expenses: "))

expenses = list(map(int, input(f"Enter {n} expenses separated by space: ").split()))

print("\n--- Expense Report ---")
print("Total Expenses:", sum(expenses))
print("Average Expense:", sum(expenses) / n)
print("Highest Expense:", max(expenses))
print("Lowest Expense:", min(expenses))
