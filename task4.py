
n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEmployee", i + 1)

    name = input("Enter employee name: ")
    basic = float(input("Enter basic salary: "))
    allowance = float(input("Enter allowances: "))
    overtime = float(input("Enter overtime amount: "))
    incentive = float(input("Enter incentives: "))

    # Gross salary
    gross = basic + allowance + overtime + incentive

    # Progressive deductions
    if gross <= 20000:
        deduction = gross * 0.05
    elif gross <= 40000:
        deduction = gross * 0.10
    else:
        deduction = gross * 0.15

    # Net salary
    net = gross - deduction

    # Salary statement
    print("\n----- SALARY STATEMENT -----")
    print("Employee Name:", name)
    print("Basic Salary:", basic)
    print("Allowances:", allowance)
    print("Overtime:", overtime)
    print("Incentives:", incentive)
    print("Gross Salary:", gross)
    print("Deduction:", deduction)
    print("Net Salary:", net)
    print("----------------------------")
