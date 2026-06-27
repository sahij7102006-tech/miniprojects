#Student Grade File Manager — Reads student data from CSV, computes grades using functions, writes updated results back to a new CSV file.by usingFunctions, modules, file I/O, exception handling, OOP basics in python
import csv

# OOP: Student Class
class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = float(marks)

    # Function to calculate grade
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"


# Manager Class
class GradeManager:

    def process_grades(self, input_file, output_file):
        try:
            students = []

            # Read CSV file
            with open(input_file, "r", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header

                for row in reader:
                    student = Student(row[0], row[1], row[2])
                    students.append(student)

            # Write updated results
            with open(output_file, "w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow(
                    ["Student ID", "Name", "Marks", "Grade"]
                )

                for student in students:
                    writer.writerow([
                        student.student_id,
                        student.name,
                        student.marks,
                        student.calculate_grade()
                    ])

            print("Grades processed successfully!")
            print("Results saved to:", output_file)

        except FileNotFoundError:
            print("Error: Input file not found.")

        except Exception as e:
            print("Error:", e)


# Main Program
manager = GradeManager()

input_file = "students.csv"
output_file = "results.csv"

manager.process_grades(input_file, output_file)
