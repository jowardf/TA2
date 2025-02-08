# Open the "students.txt" file in read mode and read its contents
try:
    with open("students.txt", "r") as file:
        student_info = file.read()

    # Display student information
    print("Reading Student Information")
    print(student_info)
except FileNotFoundError:
    print("The file 'students.txt' does not exist. No student information found.")
