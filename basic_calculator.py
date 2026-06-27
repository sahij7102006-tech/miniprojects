#Basic Calculator — Performs +, −, ×, ÷ with input validation using if-elif-else, handles division by zero.usinig variable,loops ,conditionals,strings in python
# Basic Calculator

while True:
    print("\n--- Basic Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Calculator closed.")
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
            print("Result =", result)

        elif choice == "2":
            result = num1 - num2
            print("Result =", result)

        elif choice == "3":
            result = num1 * num2
            print("Result =", result)

        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print("Result =", result)

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
