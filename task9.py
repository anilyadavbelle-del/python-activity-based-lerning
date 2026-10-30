
expenses = []

n = int(input("Enter number of expenses: "))

rate = float(input("Enter exchange rate (1 foreign unit in INR): "))
fee = float(input("Enter conversion fee percentage: "))
budget = float(input("Enter travel budget in INR: "))

for i in range(n):
    print("\nExpense", i + 1)

    name = input("Enter expense category: ")
    amount = float(input("Enter amount in foreign currency: "))

    inr = amount * rate
    charge = inr * fee / 100
    total = inr + charge

    expenses.append((name, total))

    print("Converted Amount:", inr)
    print("Conversion Fee:", charge)
    print("Total Expense:", total)

total_expense = 0

for e in expenses:
    total_expense += e[1]

print("\n--- Travel Report ---")

for e in expenses:
    print(e[0], ":", e[1])

print("Total Expense:", total_expense)

largest = max(expenses, key=lambda x: x[1])
print("Largest Expense:", largest[0])

if total_expense <= budget:
    print("Within Budget")
else:
    print("Budget Exceeded:", total_expense - budget)
