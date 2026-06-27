#Shopping Cart System — Add/remove items (list), track unique categories (set), store item-price pairs (dictionary), compute total bill.using Lists, tuples, dictionaries, sets, comprehensions in python
# Shopping Cart System

cart = []  # List to store item names

item_prices = {}  # Dictionary: item -> price
item_categories = {}  # Dictionary: item -> category

while True:
    print("\n===== SHOPPING CART =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Calculate Total Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Item
    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        category = input("Enter item category: ")

        cart.append(item)
        item_prices[item] = price
        item_categories[item] = category

        print(item, "added to cart.")

    # Remove Item
    elif choice == "2":
        item = input("Enter item to remove: ")

        if item in cart:
            cart.remove(item)
            del item_prices[item]
            del item_categories[item]
            print(item, "removed from cart.")
        else:
            print("Item not found.")

    # View Cart
    elif choice == "3":
        if cart:
            print("\nItems in Cart:")

            # List comprehension
            cart_items = [item for item in cart]

            for item in cart_items:
                print(item, "- ₹", item_prices[item])

            # Set comprehension for unique categories
            categories = {
                item_categories[item]
                for item in cart
            }

            print("\nUnique Categories:", categories)

            # Tuple list
            item_details = [
                (item, item_prices[item])
                for item in cart
            ]

            print("\nItem-Price Tuples:")
            for detail in item_details:
                print(detail)

        else:
            print("Cart is empty.")

    # Calculate Total Bill
    elif choice == "4":
        total = sum(
            price for item, price in item_prices.items()
            if item in cart
        )

        print("Total Bill = ₹", total)

    # Exit
    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice! Try again.")
