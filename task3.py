
n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nPatient", i + 1)

    name = input("Enter patient name: ")
    consultation = float(input("Enter consultation charges: "))
    diagnostic = float(input("Enter diagnostic charges: "))
    treatment = float(input("Enter treatment charges: "))

    # Validate charges
    if consultation < 0 or diagnostic < 0 or treatment < 0:
        print("Invalid charges!")
        continue

    total = consultation + diagnostic + treatment

    # Apply concession
    if total >= 10000:
        discount = total * 0.20
    elif total >= 5000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    print("\n--- Hospital Bill ---")
    print("Patient Name:", name)
    print("Total Charges:", total)
    print("Discount:", discount)
    print("Final Bill:", final_bill)

    # Patient classification
    if final_bill >= 10000:
        category = "High Payment"
    elif final_bill >= 5000:
        category = "Medium Payment"
    else:
        category = "Low Payment"

    print("Patient Category:", category)

    # Payment policy
    paid = float(input("Enter amount paid: "))

    if paid < 0 or paid > final_bill:
        print("Invalid payment amount!")
    elif paid == final_bill:
        print("Payment Completed")
    else:
        print("Pending Amount:", final_bill - paid)
