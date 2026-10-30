
plans = []

n = int(input("Enter number of mobile plans: "))

usage = float(input("Enter your data usage (GB): "))
days = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget: "))

for i in range(n):
    print("\nPlan", i + 1)

    name = input("Enter plan name: ")
    price = float(input("Enter plan price: "))
    data = float(input("Enter data limit (GB): "))
    validity = int(input("Enter validity (days): "))
    extra_rate = float(input("Enter extra charge per GB: "))

    # Calculate excess charges
    if usage > data:
        extra = (usage - data) * extra_rate
    else:
        extra = 0

    total = price + extra

    # Check eligibility
    if validity >= days and total <= budget:
        plans.append((name, total))

# Find cheapest plan
print("\n--- Plan Comparison ---")

if len(plans) > 0:
    plans.sort(key=lambda x: x[1])

    for p in plans:
        print("Plan:", p[0], "Total Cost:", p[1])

    print("\nMost Economical Plan:")
    print("Plan Name:", plans[0][0])
    print("Total Cost:", plans[0][1])
else:
    print("No eligible plan found!")
