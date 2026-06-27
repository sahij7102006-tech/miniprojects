#Library Book Management System - Add/remove/search books stored in a CSV file using file handling; functions for each operation; try-except for file not found errors.Functions, modules, file I/O, exception handling, OOP basics
import csv
import os

# OOP: Book class
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author


class Library:
    FILE_NAME = "books.csv"

    # Add a book
    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)

        with open(self.FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([book.book_id, book.title, book.author])

        print("Book added successfully!")

    # View all books
    def view_books(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                reader = csv.reader(file)

                print("\n--- Book List ---")
                for row in reader:
                    print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}")

        except FileNotFoundError:
            print("No book file found!")

    # Search a book
    def search_book(self):
        search_title = input("Enter book title to search: ")

        try:
            with open(self.FILE_NAME, "r") as file:
                reader = csv.reader(file)

                found = False

                for row in reader:
                    if row[1].lower() == search_title.lower():
                        print("\nBook Found:")
                        print("ID:", row[0])
                        print("Title:", row[1])
                        print("Author:", row[2])
                        found = True
                        break

                if not found:
                    print("Book not found.")

        except FileNotFoundError:
            print("No book file found!")

    # Remove a book
    def remove_book(self):
        remove_id = input("Enter Book ID to remove: ")

        try:
            books = []

            with open(self.FILE_NAME, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row[0] != remove_id:
                        books.append(row)

            with open(self.FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(books)

            print("Book removed successfully!")

        except FileNotFoundError:
            print("No book file found!")


# Main Program
library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.remove_book()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
