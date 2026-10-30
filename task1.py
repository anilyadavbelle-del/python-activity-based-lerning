
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter name: ")
    marks = float(input("Enter aggregate marks: "))
    
    s1 = float(input("Enter subject 1 marks: "))
    s2 = float(input("Enter subject 2 marks: "))
    s3 = float(input("Enter subject 3 marks: "))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter family income: "))

    # Eligibility checking
    if (marks >= 75 and s1 >= 50 and s2 >= 50
        and s3 >= 50 and attendance >= 75
        and income <= 200000):

        students.append((name, marks, attendance, income))
        print(name, "is Eligible")

    else:
        print(name, "is Not Eligible")

# Ranking students
students.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n--- Scholarship Ranking ---")

for i, student in enumerate(students, 1):
    print(i, student[0], "Marks:", student[1],
          "Attendance:", student[2],
          "Income:", student[3])
