#Contact Book (CLI) — Add, search, update, delete contacts stored in a dictionary. Uses sets to detect duplicate numbers.using Lists, tuples, dictionaries, sets, comprehensions in python
# Contact Book (CLI)

contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        # Set for duplicate detection
        phone_numbers = set(contacts.values())

        if phone in phone_numbers:
            print("Duplicate phone number detected!")
        else:
            contacts[name] = phone
            print("Contact added successfully.")

    # Search Contact
    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    # Update Contact
    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            new_phone = input("Enter new phone number: ")

            phone_numbers = set(contacts.values())

            if new_phone in phone_numbers and new_phone != contacts[name]:
                print("Duplicate phone number detected!")
            else:
                contacts[name] = new_phone
                print("Contact updated successfully.")
        else:
            print("Contact not found.")

    # Delete Contact
    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    # View All Contacts
    elif choice == "5":
        if contacts:
            print("\nAll Contacts:")

            # List comprehension
            contact_list = [name for name in contacts]

            for name in contact_list:
                print(name, ":", contacts[name])

            # Tuple comprehension style display
            contact_tuples = [(name, phone)
                              for name, phone in contacts.items()]

            print("\nContacts as Tuples:")
            for item in contact_tuples:
                print(item)

        else:
            print("No contacts available.")

    # Exit
    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice! Try again.")
