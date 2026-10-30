
n = int(input("Enter number of passengers: "))

total = 0

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter travel distance (KM): "))
    travel_class = input("Enter class (sleeper/AC): ").lower()

    # Distance fare
    if distance <= 100:
        rate = 1
    elif distance <= 500:
        rate = 2
    else:
        rate = 3

    fare = distance * rate

    # Travel class charges
    if travel_class == "ac":
        fare = fare * 2
    elif travel_class == "sleeper":
        fare = fare
    else:
        print("Invalid class!")
        continue

    # Age concession
    if age >= 60:
        discount = fare * 0.20
    elif age <= 12:
        discount = fare * 0.50
    else:
        discount = 0

    reservation = 50

    final_fare = fare - discount + reservation

    print("\n--- Passenger Ticket ---")
    print("Name:", name)
    print("Distance:", distance, "KM")
    print("Class:", travel_class)
    print("Base Fare:", fare)
    print("Concession:", discount)
    print("Reservation Fee:", reservation)
    print("Final Fare:", final_fare)

    total = total + final_fare

print("\nTotal Reservation Amount:", total)

# Cancellation calculation
cancel = input("\nDo you want to cancel ticket? (yes/no): ").lower()

if cancel == "yes":
    penalty = total * 0.25
    refund = total - penalty

    print("Cancellation Penalty:", penalty)
    print("Refund Amount:", refund)
else:
    print("Reservation Confirmed")
