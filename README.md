#Simple-University-Attendance-System
Project Overview:
The project is a command-line based Simple University Attendance System developed in Python. It allows a user to add students, mark students as present or absent, view an individual student's attendance details, and view attendance information for all students.
The uploaded course instructions state that the project must be executable through the command line, and that the repository should include a README.md with setup, dependency, configuration, and execution instructions. The instructions also require a structured project report.
Main Features:
The program consists of several main features for managing student attendance. The Add Student feature stores the student’s roll number and name and initializes their present and absent counts to zero in the students dictionary. The Mark Attendance feature updates the student’s present or absent count based on the P/A input provided by the user. The View One Student feature calculates and displays the total attendance and attendance percentage for an individual student using the formula (present / total) × 100. The View All Students feature loops through all the students stored in the dictionary and displays their attendance information. Finally, the Exit feature terminates the menu-driven program when the user selects option 5.
Requirements:
The uploaded project is a basic Python command-line program. No external Python package is used in the supplied source code.
Python 3.x
A terminal/command prompt
The uploaded Python source file: Vityarthi_Project.py
No GUI-based setup is required to execute the supplied program.
How to Run the Project:
Install Python 3.x on the computer if it is not already installed.
Open Command Prompt or another terminal.
Navigate to the folder containing Vityarthi_Project.py.
Run the program with: python Vityarthi_Project.py
Use the displayed menu to add students and manage attendance.
Testing:
The program is tested using several test cases to verify that all major functions work correctly. First, the Add Student function is tested by entering the roll number and name through Menu 1, with the expected result being that the student is added successfully. The Mark Present and Mark Absent functions are tested through Menu 2 using P and A inputs, respectively, and the corresponding present or absent count should increase by one. The View Student function is tested by entering a valid roll number through Menu 3, where the student’s attendance details and percentage should be displayed. An Invalid Student test is performed using an unknown roll number, which should display a student-not-found message. Finally, an Invalid Status test is performed by entering a value other than P or A, which should display an invalid-input message. The supplied source code supports the expected behavior described above, while the actual execution results should be verified by running the program in the target terminal environment.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/424e0b50-15a6-4207-86fc-2a7e4bcace04" />
