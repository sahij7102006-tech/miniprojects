#Student Result Management System - Store student names and marks in a dictionary, compute average, find topper, display grade using list comprehensions using Lists, tuples, dictionaries, sets, comprehensions in python
# Student Result Management System

# Dictionary: Student Name -> Marks
students = {
    "Aman": 85,
    "Riya": 92,
    "Karan": 78,
    "Neha": 95,
    "Simran": 88
}

# Display all students
print("Student Records:")
for name, marks in students.items():
    print(name, ":", marks)

# Average Marks
average = sum(students.values()) / len(students)
print("\nAverage Marks:", average)

# Find Topper
topper = max(students, key=students.get)
print("Topper:", topper)
print("Top Marks:", students[topper])

# Function to assign grades
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "D"

# Dictionary Comprehension for Grades
grades = {name: get_grade(marks) for name, marks in students.items()}

print("\nStudent Grades:")
for name, grade in grades.items():
    print(name, ":", grade)

# List Comprehension: Students scoring above average
above_average = [name for name, marks in students.items() if marks > average]
print("\nStudents Above Average:", above_average)

# Tuple: Store topper details
topper_details = (topper, students[topper])
print("Topper Details (Tuple):", topper_details)

# Set: Unique Grades
unique_grades = {grade for grade in grades.values()}
print("Unique Grades (Set):", unique_grades)
