
n = int(input("Enter number of products: "))

total = 0

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    category = input("Enter category (food/electronics/other): ")

    amount = price * qty

    if category == "food":
        tax = amount * 0.05
    elif category == "electronics":
        tax = amount * 0.18
    else:
        tax = amount * 0.10

    bill = amount + tax

    if bill >= 5000:
        discount = bill * 0.20
    elif bill >= 2000:
        discount = bill * 0.10
    else:
        discount = 0

    if discount > 1000:
        discount = 1000

    final = bill - discount
    total = total + final

    print("Product:", name)
    print("Amount:", amount)
    print("Tax:", tax)
    print("Discount:", discount)
    print("Final Price:", final)

print("\nTotal Bill:", total)
