# Assignment 1: Student Data Management using Dictionary, Tuple and List

students = []

# Add a new student
roll_no = int(input("Enter Roll Number: "))
name = input("Enter Name: ")
branch = input("Enter Branch: ")
marks = float(input("Enter Marks: "))

student = {
    "Roll No": roll_no,
    "Name": name,
    "Branch": branch,
    "Marks": marks
}

students.append(student)

# Delete a student
delete_roll = int(input("\nEnter Roll Number to delete: "))

for student in students:
    if student["Roll No"] == delete_roll:
        students.remove(student)
        print("Student deleted successfully.")
        break
else:
    print("Student not found.")

# Update a student
update_roll = int(input("\nEnter Roll Number to update: "))

for student in students:
    if student["Roll No"] == update_roll:
        student["Name"] = input("Enter new Name: ")
        student["Branch"] = input("Enter new Branch: ")
        student["Marks"] = float(input("Enter new Marks: "))
        print("Student updated successfully.")
        break
else:
    print("Student not found.")

# Display records
print("\nFinal Student Records:")

for student in students:
    print(student)
