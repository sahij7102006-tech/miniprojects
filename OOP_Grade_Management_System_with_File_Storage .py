#OOP Grade Management System with File Storage - Classes for Student, Teacher, Course; inheritance and polymorphism; stores/retrieves records from file using _str_ dunder method. by using Inheritance, polymorphism, decorators, regex, generators in python
import re

# Base Class
class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def display_role(self):
        return "Person"

    def __str__(self):
        return f"{self.person_id},{self.name},{self.display_role()}"


# Inheritance: Student Class
class Student(Person):
    def __init__(self, person_id, name, marks):
        super().__init__(person_id, name)
        self._marks = marks

    # Decorator
    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Marks must be between 0 and 100")

    def display_role(self):
        return "Student"

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        return "F"

    def __str__(self):
        return (
            f"{self.person_id},{self.name},"
            f"{self.marks},{self.grade()},Student"
        )


# Inheritance: Teacher Class
class Teacher(Person):
    def __init__(self, person_id, name, subject):
        super().__init__(person_id, name)
        self.subject = subject

    def display_role(self):
        return "Teacher"

    def __str__(self):
        return (
            f"{self.person_id},{self.name},"
            f"{self.subject},Teacher"
        )


# Course Class
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    # Generator
    def student_generator(self):
        for student in self.students:
            yield student

    def show_students(self):
        print(f"\nCourse: {self.course_name}")
        for student in self.student_generator():
            print(student)


# File Manager Class
class FileManager:

    FILE_NAME = "records.txt"

    def save_record(self, obj):
        with open(self.FILE_NAME, "a") as file:
            file.write(str(obj) + "\n")

    def display_records(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                print("\n--- Stored Records ---")
                for line in file:
                    print(line.strip())

        except FileNotFoundError:
            print("No records found.")


# Main Program
course = Course("Python Programming")
file_manager = FileManager()

while True:
    print("\n===== GRADE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. View Course Students")
    print("4. View Saved Records")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        student_id = input("Enter Student ID (S001): ")

        # Regex Validation
        if not re.match(r"^S\d{3}$", student_id):
            print("Invalid Student ID format!")
            continue

        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = Student(student_id, name, marks)

        course.add_student(student)
        file_manager.save_record(student)

        print("Student added successfully!")

    elif choice == "2":

        teacher_id = input("Enter Teacher ID (T001): ")

        if not re.match(r"^T\d{3}$", teacher_id):
            print("Invalid Teacher ID format!")
            continue

        name = input("Enter Name: ")
        subject = input("Enter Subject: ")

        teacher = Teacher(teacher_id, name, subject)

        file_manager.save_record(teacher)

        print("Teacher added successfully!")

    elif choice == "3":
        course.show_students()

    elif choice == "4":
        file_manager.display_records()

    elif choice == "5":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
