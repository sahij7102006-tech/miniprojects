#Simple ATM Machine — User enters PIN, can check balance, deposit, or withdraw. Uses conditionals and loops for menu navigation.usinig variable,loops ,conditionals,strings inpython

# Simple ATM Machine

correct_pin = "1234"
balance = 1000

print("Welcome to the ATM")

pin = input("Enter your PIN: ")

if pin == correct_pin:
    while True:
        print("\n----- ATM Menu -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Your balance is ₹", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: ₹"))
            balance += amount
            print("Deposit successful!")
            print("New balance: ₹", balance)

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= balance:
                balance -= amount
                print("Withdrawal successful!")
                print("Remaining balance: ₹", balance)
            else:
                print("Insufficient balance!")

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice! Please try again.")

else:
    print("Incorrect PIN. Access denied.")
