#Bank Account System (OOP) — Base class Account, child classes SavingsAccount and CurrentAccount with overridden withdraw() method; encapsulation of balance; regex to validate account numbers.. by using Inheritance, polymorphism, decorators, regex, generators in python
import re

# Base Class
class Account:
    def __init__(self, account_no, holder_name, balance):

        # Regex Validation
        if not re.match(r"^ACC\d{4}$", account_no):
            raise ValueError(
                "Invalid Account Number! Format: ACC1234"
            )

        self.account_no = account_no
        self.holder_name = holder_name
        self.__balance = balance  # Encapsulation

    # Decorator (Getter)
    @property
    def balance(self):
        return self.__balance

    # Decorator (Setter)
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative.")

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def __str__(self):
        return (
            f"Account No: {self.account_no}, "
            f"Name: {self.holder_name}, "
            f"Balance: ₹{self.balance}"
        )


# Child Class - Savings Account
class SavingsAccount(Account):

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(
                f"Savings Account: ₹{amount} withdrawn."
            )


# Child Class - Current Account
class CurrentAccount(Account):

    def withdraw(self, amount):
        overdraft_limit = 5000

        if amount <= self.balance + overdraft_limit:
            self.balance -= amount
            print(
                f"Current Account: ₹{amount} withdrawn."
            )
        else:
            print("Overdraft limit exceeded.")


# Generator Function
def account_generator(accounts):
    for account in accounts:
        yield account


# Main Program
accounts = []

while True:
    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. View Accounts")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            acc_no = input("Enter Account Number (ACC1234): ")
            name = input("Enter Holder Name: ")
            balance = float(input("Enter Initial Balance: "))

            account = SavingsAccount(
                acc_no, name, balance
            )

            accounts.append(account)
            print("Savings Account Created.")

        elif choice == "2":
            acc_no = input("Enter Account Number (ACC1234): ")
            name = input("Enter Holder Name: ")
            balance = float(input("Enter Initial Balance: "))

            account = CurrentAccount(
                acc_no, name, balance
            )

            accounts.append(account)
            print("Current Account Created.")

        elif choice == "3":

            print("\n--- Account Details ---")
            for account in account_generator(accounts):
                print(account)

        elif choice == "4":

            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Deposit Amount: "))

            for account in accounts:
                if account.account_no == acc_no:
                    account.deposit(amount)

        elif choice == "5":

            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Withdraw Amount: "))

            for account in accounts:
                if account.account_no == acc_no:
                    account.withdraw(amount)

        elif choice == "6":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice.")

    except ValueError as e:
        print("Error:", e)
