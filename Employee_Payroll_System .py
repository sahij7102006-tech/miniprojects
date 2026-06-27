#Employee Payroll System — Employee → FullTimeEmployee / PartTimeEmployee with polymorphic calculate_salary(); decorator to log every salary computation; export to file.by using Inheritance, polymorphism, decorators, regex, generators in python
import re
from datetime import datetime

# Decorator for logging salary calculations
def salary_logger(func):
    def wrapper(self):
        salary = func(self)

        log_message = (
            f"{datetime.now()} | "
            f"{self.emp_id} | "
            f"{self.name} | "
            f"Salary = ₹{salary}\n"
        )

        with open("salary_log.txt", "a") as file:
            file.write(log_message)

        return salary

    return wrapper


# Base Class
class Employee:

    def __init__(self, emp_id, name):

        # Regex Validation
        if not re.match(r"^EMP\d{3}$", emp_id):
            raise ValueError(
                "Invalid Employee ID! Format: EMP001"
            )

        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        pass

    def __str__(self):
        return f"{self.emp_id} - {self.name}"


# Child Class: Full-Time Employee
class FullTimeEmployee(Employee):

    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary

    @salary_logger
    def calculate_salary(self):
        return self.monthly_salary


# Child Class: Part-Time Employee
class PartTimeEmployee(Employee):

    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)

        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    @salary_logger
    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


# Generator
def employee_generator(employee_list):
    for employee in employee_list:
        yield employee


# Payroll Manager
class PayrollSystem:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_payroll(self):

        print("\n----- PAYROLL REPORT -----")

        for employee in employee_generator(self.employees):

            salary = employee.calculate_salary()

            print(
                f"ID: {employee.emp_id}, "
                f"Name: {employee.name}, "
                f"Salary: ₹{salary}"
            )

    def export_payroll(self):

        with open("payroll_report.txt", "w") as file:

            file.write("PAYROLL REPORT\n")
            file.write("-" * 40 + "\n")

            for employee in employee_generator(self.employees):

                salary = employee.calculate_salary()

                file.write(
                    f"{employee.emp_id}, "
                    f"{employee.name}, "
                    f"₹{salary}\n"
                )

        print("Payroll exported successfully!")


# Main Program
payroll = PayrollSystem()

while True:

    print("\n===== EMPLOYEE PAYROLL SYSTEM =====")
    print("1. Add Full-Time Employee")
    print("2. Add Part-Time Employee")
    print("3. Display Payroll")
    print("4. Export Payroll")
    print("5. Exit")

    choice = input("Enter choice: ")

    try:

        if choice == "1":

            emp_id = input("Employee ID (EMP001): ")
            name = input("Name: ")
            salary = float(
                input("Monthly Salary: ")
            )

            emp = FullTimeEmployee(
                emp_id,
                name,
                salary
            )

            payroll.add_employee(emp)

            print("Full-Time Employee Added!")

        elif choice == "2":

            emp_id = input("Employee ID (EMP001): ")
            name = input("Name: ")

            hours = float(
                input("Hours Worked: ")
            )

            rate = float(
                input("Hourly Rate: ")
            )

            emp = PartTimeEmployee(
                emp_id,
                name,
                hours,
                rate
            )

            payroll.add_employee(emp)

            print("Part-Time Employee Added!")

        elif choice == "3":

            payroll.display_payroll()

        elif choice == "4":

            payroll.export_payroll()

        elif choice == "5":

            print("Program Ended.")
            break

        else:
            print("Invalid Choice!")

    except ValueError as e:
        print("Error:", e)
