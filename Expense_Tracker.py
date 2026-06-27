#Expense Tracker — Log daily expenses to a .txt file, read and summarize by category using functions; handles invalid input via exception handling. by usingFunctions, modules, file I/O, exception handling, OOP basics
# Expense Tracker

from datetime import datetime

# OOP: Expense Class
class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount


class ExpenseTracker:
    FILE_NAME = "expenses.txt"

    # Add expense
    def add_expense(self):
        try:
            category = input("Enter category (Food, Travel, Shopping, etc.): ")
            amount = float(input("Enter amount: ₹"))

            expense = Expense(category, amount)

            with open(self.FILE_NAME, "a") as file:
                file.write(
                    f"{datetime.now().date()},{expense.category},{expense.amount}\n"
                )

            print("Expense added successfully!")

        except ValueError:
            print("Invalid amount! Please enter a number.")

    # View all expenses
    def view_expenses(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                print("\n--- Expense Records ---")
                for line in file:
                    date, category, amount = line.strip().split(",")
                    print(
                        f"Date: {date} | Category: {category} | Amount: ₹{amount}"
                    )

        except FileNotFoundError:
            print("No expense file found.")

    # Summarize expenses by category
    def summarize_expenses(self):
        try:
            summary = {}

            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    date, category, amount = line.strip().split(",")

                    if category in summary:
                        summary[category] += float(amount)
                    else:
                        summary[category] = float(amount)

            print("\n--- Expense Summary ---")
            total = 0

            for category, amount in summary.items():
                print(f"{category}: ₹{amount}")
                total += amount

            print("Total Expenses: ₹", total)

        except FileNotFoundError:
            print("No expense file found.")


# Main Program
tracker = ExpenseTracker()

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tracker.add_expense()

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.summarize_expenses()

    elif choice == "4":
        print("Exiting Expense Tracker...")
        break

    else:
        print("Invalid choice! Try again.")
