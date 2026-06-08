students = []

while True:
    print("\n===== Attendance Management System =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append({"name": name, "attendance": "Not Marked"})
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students available.")
        else:
            print("\nMark Attendance")
            for student in students:
                status = input(f"{student['name']} (P/A): ").upper()
                if status in ["P", "A"]:
                    student["attendance"] = status
                else:
                    print("Invalid input! Marked as Absent.")
                    student["attendance"] = "A"

    elif choice == "3":
        if len(students) == 0:
            print("No records found.")
        else:
            print("\nAttendance Records")
            print("-" * 30)
            print("Name\t\tAttendance")
            print("-" * 30)
            for student in students:
                print(f"{student['name']}\t\t{student['attendance']}")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")