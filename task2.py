
bills = []

n = int(input("Enter number of months: "))

for i in range(n):
    print("\nMonth", i + 1)

    units = float(input("Enter electricity units: "))

    # Calculate slab charges
    if units <= 100:
        amount = units * 2
    elif units <= 200:
        amount = 100 * 2 + (units - 100) * 3
    elif units <= 300:
        amount = 100 * 2 + 100 * 3 + (units - 200) * 5
    else:
        amount = 100 * 2 + 100 * 3 + 100 * 5 + (units - 300) * 7

    fixed = 50
    surcharge = amount * 0.05

    total = amount + fixed + surcharge

    # Rebate for low consumption
    if units <= 100:
        rebate = total * 0.10
    else:
        rebate = 0

    final_bill = total - rebate

    bills.append(final_bill)

    print("Electricity Bill:", round(final_bill, 2))

# Monthly comparison
print("\n--- Monthly Bill Comparison ---")

for i in range(n):
    print("Month", i + 1, "Bill:", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]

        if increase > bills[i - 1] * 0.20:
            print("Unusual Increase Detected!")
        else:
            print("Normal Bill")
