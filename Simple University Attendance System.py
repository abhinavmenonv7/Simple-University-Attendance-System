# Simple University Attendance System

students = {}

while True:

    print("\n===== ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Student Attendance")
    print("4. View All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":

        roll = input("Enter Roll Number (Example: CSE101): ").upper()
        name = input("Enter Student Name: ")

        students[roll] = {
            "name": name,
            "present": 0,
            "absent": 0
        }

        print("Student added successfully!")

    # Mark Attendance
    elif choice == "2":

        roll = input("Enter Roll Number: ").upper()

        if roll in students:

            status = input("Enter P for Present or A for Absent: ").upper()

            if status == "P":
                students[roll]["present"] += 1
                print("Attendance marked as Present.")

            elif status == "A":
                students[roll]["absent"] += 1
                print("Attendance marked as Absent.")

            else:
                print("Invalid input. Enter P or A.")

        else:
            print("Student not found.")

    # View One Student
    elif choice == "3":

        roll = input("Enter Roll Number: ").upper()

        if roll in students:

            name = students[roll]["name"]
            present = students[roll]["present"]
            absent = students[roll]["absent"]

            total = present + absent

            if total > 0:
                percentage = (present / total) * 100
            else:
                percentage = 0

            print("\n--- Student Attendance ---")
            print("Name:", name)
            print("Roll Number:", roll)
            print("Present:", present)
            print("Absent:", absent)
            print("Attendance:", round(percentage, 2), "%")

        else:
            print("Student not found.")

    # View All Students
    elif choice == "4":

        if len(students) == 0:
            print("No students found.")

        else:

            print("\n========== ALL STUDENTS ==========")

            for roll, student in students.items():

                name = student["name"]
                present = student["present"]
                absent = student["absent"]

                total = present + absent

                if total > 0:
                    percentage = (present / total) * 100
                else:
                    percentage = 0

                print("\nName:", name)
                print("Roll Number:", roll)
                print("Present:", present)
                print("Absent:", absent)