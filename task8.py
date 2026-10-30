
material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
machine = float(input("Enter machine cost: "))
wastage = float(input("Enter wastage percentage: "))
selling = float(input("Enter selling price: "))
target = float(input("Enter profit target: "))

waste_cost = material * wastage / 100

total_cost = material + labour + machine + waste_cost

profit = selling - total_cost

print("\n--- Manufacturing Report ---")
print("Material Cost:", material)
print("Labour Cost:", labour)
print("Machine Cost:", machine)
print("Wastage Cost:", waste_cost)
print("Total Cost:", total_cost)
print("Selling Price:", selling)
print("Profit:", profit)

if profit >= target:
    print("Profit Target Achieved")
else:
    print("Profit Target Not Achieved")

