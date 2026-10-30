
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per person: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per person: "))

participants = int(input("Enter number of participants: "))
sponsor = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per person: "))

# Total cost
fixed = venue + equipment + transport
variable = participants * (catering + certificate)

total = fixed + variable

# Total income
income = sponsor + participants * fee

print("\n--- Event Financial Report ---")
print("Fixed Cost:", fixed)
print("Variable Cost:", variable)
print("Total Cost:", total)
print("Total Income:", income)

if income >= total:
    print("Event is Profitable")
else:
    print("Sponsorship Shortfall:", total - income)

# Break-even participants
contribution = fee - catering - certificate

if contribution > 0:
    minimum = fixed / contribution
    minimum = int(minimum)
    if minimum < fixed / contribution:
        minimum += 1

    print("Minimum Participants:", minimum)
else:
    print("Break-even is not possible with this registration fee")
