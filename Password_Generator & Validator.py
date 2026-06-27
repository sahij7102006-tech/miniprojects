#	Password Generator & Validator — Generates random strong passwords using random and string modules; validates user-entered passwords with custom exception if rules not met..by usingFunctions, modules, file I/O, exception handling, OOP basics in python
import random
import string

# Custom Exception
class PasswordError(Exception):
    pass


# OOP Class
class PasswordManager:

    # Generate Password
    def generate_password(self, length=12):
        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ''.join(
            random.choice(characters)
            for _ in range(length)
        )

        return password

    # Validate Password
    def validate_password(self, password):

        if len(password) < 8:
            raise PasswordError(
                "Password must be at least 8 characters long."
            )

        if not any(char.isupper() for char in password):
            raise PasswordError(
                "Password must contain at least one uppercase letter."
            )

        if not any(char.islower() for char in password):
            raise PasswordError(
                "Password must contain at least one lowercase letter."
            )

        if not any(char.isdigit() for char in password):
            raise PasswordError(
                "Password must contain at least one digit."
            )

        if not any(char in string.punctuation for char in password):
            raise PasswordError(
                "Password must contain at least one special character."
            )

        return True

    # Save Password to File
    def save_password(self, password):
        with open("passwords.txt", "a") as file:
            file.write(password + "\n")


# Main Program
manager = PasswordManager()

while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Generate Password")
    print("2. Validate Password")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        password = manager.generate_password()

        print("Generated Password:", password)

        manager.save_password(password)
        print("Password saved to passwords.txt")

    elif choice == "2":
        try:
            password = input("Enter password: ")

            if manager.validate_password(password):
                print("Strong Password ✔")

        except PasswordError as e:
            print("Validation Error:", e)

    elif choice == "3":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice!")
